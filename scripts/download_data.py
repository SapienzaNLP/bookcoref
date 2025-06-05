from pathlib import Path
from typing import Literal

from datasets import DatasetDict, load_dataset
from rich import print
from tap import Tap


class ScriptArgs(Tap):
    """
    Script that downloads BOOKCOREF from HuggingFace in either JSONL or CoNLL format.
    """
    format: Literal["jsonl", "conll"] = "jsonl"  # Format of the dataset to download, either 'jsonl' or 'conll'
    test_only: bool = False  # If True, only download the test set
    output_dir: Path = Path("data/") # Default output directory for the dataset

    def process_args(self) -> None:
        """
        Process the command line arguments.
        """
        self.output_dir.mkdir(parents=True, exist_ok=True)

BOOKCOREF_HF_REPO = "tommasobonomo/bookcoref"

def main(args: ScriptArgs):
    """
    Main function to download the BOOKCOREF dataset from Hugging Face.
    """

    print(f"[bold green]Downloading BOOKCOREF dataset in {args.format} format...[/bold green]")
    print(f"Output directory: [bold blue]{args.output_dir}[/bold blue]")

    if args.test_only:
        print("[bold green]Downloading only `test.jsonl` and `test_splitted.jsonl`...[/bold green]")
        dataset: DatasetDict = DatasetDict({
            "test": load_dataset(BOOKCOREF_HF_REPO, split="test"),
            "test_splitted": load_dataset(BOOKCOREF_HF_REPO, split="test_splitted"),
        })
    else:
        print("[bold green]Downloading all splits of the dataset...[/bold green]")
        dataset: DatasetDict = load_dataset(BOOKCOREF_HF_REPO) # type: ignore
    print(f"[bold green]Dataset loaded with splits: {list(dataset.keys())}[/bold green]")


    match args.format:
        case "jsonl":
            print("[bold green]Saving dataset in JSONL format...[/bold green]")
            for split in dataset:
                dataset[split].to_json(args.output_dir / f"{split}.jsonl")

        case "conll":
            raise NotImplementedError("CoNLL format is not yet implemented.")

    print(f"[bold green]Dataset saved to[/bold green] [bold blue]{args.output_dir}[/bold blue]")

if __name__ == "__main__":
    args = ScriptArgs().parse_args()
    main(args)