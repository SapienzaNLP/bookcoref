import json
from pathlib import Path
from typing import Literal

from datasets import DatasetDict, load_dataset
from rich import print
from tap import Tap

from src.metrics import OfficialCoNLL2012CorefEvaluator


class ScriptArgs(Tap):
    """
    Script that evaluates predictions on the BOOKCOREF test set.
    """

    predictions: Path  # Path to the predictions file in JSONL format
    mode: Literal["full", "splitted", "gold_window"] = "full"  # Mode of evaluation as explained in the paper


def main(args):
    if args.mode == "full" or args.mode == "gold_window":
        bookcoref: DatasetDict = load_dataset("sapienzanlp/bookcoref")  # type: ignore
    elif args.mode == "splitted":
        bookcoref: DatasetDict = load_dataset("sapienzanlp/bookcoref", "splitted")  # type: ignore
    else:
        raise ValueError(f"Unsupported mode: {args.mode}. Supported modes are 'full', 'splitted' and 'gold_window'.")

    gold = bookcoref["test"].to_list()

    predicted = []
    with open(args.predictions, "r") as fin:
        for elem in fin.readlines():
            predicted.append(json.loads(elem))

    if args.mode == "gold_window":
        evaluate_splitted(gold, predicted, length=1500)
    else:
        evaluate(gold, predicted)


def print_results(results):
    # Format results to 3 decimal places
    print("[bold green]Evaluation Results:[/bold green]")
    for metric, values in results.items():
        print(f"[bold blue]{metric}[/bold blue]:")
        for k, v in values.items():
            print(f"  {k}: {(100 * v):.2f}")


def evaluate(gold_elements_list, predicted_elements_list):
    results = {}
    gold = []
    predictions = []
    evaluator = OfficialCoNLL2012CorefEvaluator()

    for gold_doc_elem, pred_doc_elem in zip(gold_elements_list, predicted_elements_list):
        gold_doc_clusters = []
        for cluster in gold_doc_elem["clusters"]:
            elem = tuple([(span[0], span[1]) for span in cluster])
            gold_doc_clusters.append(elem)
        gold.append(gold_doc_clusters)

        pred_doc_clusters = []
        for cluster in pred_doc_elem["clusters"]:
            elem = tuple([(span[0], span[1]) for span in cluster])
            pred_doc_clusters.append(elem)
        predictions.append(pred_doc_clusters)

    mention_to_gold = [extract_mentions_to_clusters([tuple(g) for g in gg]) for gg in gold]
    mention_to_predicted = [extract_mentions_to_clusters([tuple(p) for p in pp]) for pp in predictions]

    results = {}
    for p, g, m2p, m2g in zip(predictions, gold, mention_to_predicted, mention_to_gold):
        evaluator.update(p, g, m2p, m2g)
    for metric in ["muc", "b_cubed", "ceafe", "conll2012"]:
        results[metric] = dict(zip(["precision", "recall", "f1"], evaluator.get_prf(metric)))

    print_results(results)


def extract_mentions_to_clusters(gold_clusters):
    mention_to_gold = {}
    for gc in gold_clusters:
        for mention in gc:
            mention_to_gold[mention] = gc
    return mention_to_gold


def evaluate_splitted(gold_elements_list, predicted_elements_list, length):
    """Evaluates full predictions on splitted BOOKCOREF test set."""
    results = {}
    gold = []
    predictions = []
    evaluator = OfficialCoNLL2012CorefEvaluator()

    for gold_doc_elem, pred_doc_elem in zip(gold_elements_list, predicted_elements_list):
        sets = [
            (i + 1) * length
            for i in range(int(len([item for sublist in gold_doc_elem["sentences"] for item in sublist]) / length))
        ]

        sets.append(len([item for sublist in gold_doc_elem["sentences"] for item in sublist]))

        for s in sets:
            gold_doc_clusters = []
            for cluster in gold_doc_elem["clusters"]:
                elem = tuple([(span[0], span[1]) for span in cluster if span[0] > (s - length) and span[0] < s])
                if len(elem) > 0:
                    gold_doc_clusters.append(elem)
            gold.append(gold_doc_clusters)

            pred_doc_clusters = []
            for cluster in pred_doc_elem["clusters"]:
                elem = tuple([(span[0], span[1]) for span in cluster if span[0] > (s - length) and span[0] < s])
                if len(elem) > 0:
                    pred_doc_clusters.append(elem)
            predictions.append(pred_doc_clusters)

    mention_to_gold = [extract_mentions_to_clusters([tuple(g) for g in gg]) for gg in gold]
    mention_to_predicted = [extract_mentions_to_clusters([tuple(p) for p in pp]) for pp in predictions]

    results = {}
    for p, g, m2p, m2g in zip(predictions, gold, mention_to_predicted, mention_to_gold):
        evaluator.update(p, g, m2p, m2g)
    for metric in ["muc", "b_cubed", "ceafe", "conll2012"]:
        results[metric] = dict(zip(["precision", "recall", "f1"], evaluator.get_prf(metric)))

    print_results(results)


if __name__ == "__main__":
    args = ScriptArgs().parse_args()
    main(args)
