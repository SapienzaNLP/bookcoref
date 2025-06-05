from pathlib import Path
from typing import Literal

from tap import Tap


class ScriptArgs(Tap):
    """
    Command line arguments for the script.
    """
    format: Literal["jsonl", "conll"] = "jsonl"  # Format of the dataset to download, either 'jsonl' or 'conll'
    test_only: bool = False  # If True, only download the test set
    output_dir: Path = Path("data") # Default output directory for the dataset


def main(args: ScriptArgs):
    """
    Main function to download the dataset.
    """



    pass

if __name__ == "__main__":
    args = ScriptArgs().parse_args()
    main(args)