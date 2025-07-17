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
    configuration: Literal["default", "splitted"] = "default"  # Configuration of the dataset, either 'default' or 'splitted'
    output_dir: Path = Path("data/") # Default output directory for the dataset

    def process_args(self) -> None:
        """
        Process the command line arguments.
        """
        self.output_dir.mkdir(parents=True, exist_ok=True)

BOOKCOREF_HF_REPO = "sapienzanlp/bookcoref"

def main(args: ScriptArgs):
    """
    Main function to download the BOOKCOREF dataset from Hugging Face.
    """

    print(f"[bold green]Downloading BOOKCOREF dataset in {args.format} format...[/bold green]")
    print(f"Output directory: [bold blue]{args.output_dir}[/bold blue]")

    if args.configuration == "default":
        dataset: DatasetDict = load_dataset(BOOKCOREF_HF_REPO)  # type: ignore
    elif args.configuration == "splitted":
        dataset: DatasetDict = load_dataset(BOOKCOREF_HF_REPO, "splitted")  # type: ignore
    else:
        raise ValueError(f"Unsupported configuration: {args.configuration}. Supported configurations are 'default' and 'splitted'.")


    if args.format == "jsonl":
        print("[bold green]Saving dataset in JSONL format...[/bold green]")
        for split in dataset:
            dataset[split].to_json(args.output_dir / f"{split}.jsonl", orient="records", lines=True)
    elif args.format == "conll":
        raise NotImplementedError("CoNLL format is not yet implemented.")
    else:
        raise ValueError(f"Unsupported format: {args.format}. Supported formats are 'jsonl' and 'conll'.")

    print(f"[bold green]Dataset saved to[/bold green] [bold blue]{args.output_dir}[/bold blue]")

if __name__ == "__main__":
    args = ScriptArgs().parse_args()
    main(args)