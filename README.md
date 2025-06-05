<div align="center">
  <img src="assets/bookcoref.png" width="700">

</div>

<div align="center">



[![Conference](http://img.shields.io/badge/ACL-2025-4b44ce.svg)](https://20245aclweb.org/)
[![Paper](http://img.shields.io/badge/paper-ACL--anthology-B31B1B.svg)](https://aclanthology.org/)
[![Hugging Face Dataset](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-FCD21D)](https://huggingface.co/collections/sapienzanlp/relik-retrieve-read-and-link-665d9e4a5c3ecba98c1bef19)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-green.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
</div>


##  Description
This repository contains the official code for "<span style="font-variant: small-caps;">BookCoref</span>: Coreference Resolution at Book Scale" by [Martinelli et al., 2025]().
We include the official outputs of the comparison systems outlined in the paper, which can be used to reproduce our results.
Our silver training and gold evaluation data can also be found on [🤗 Hugging Face](https://huggingface.co/datasets/sapienzanlp/bookcoref).


## Setup 

First of all, clone the repository: 
```bash
git clone https://github.com/sapienzanlp/bookcoref.git
```

We offer two ways to run the scripts in this repository: using [`uv`](https://astral.sh/uv) or manually setting up a Python environment through [`conda`](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html).
If you opt for the manual setup, follow these steps:
```bash
cd bookcoref
conda create -n bookcoref python=3.12
conda activate bookcoref
pip install -r requirements.txt
```

If you use `uv`, you can run the scripts directly using `uv run <script_name.py>`.
Otherwise, you can run the scripts manually by executing: `python <script_name.py>`

## BookCoref Data 
  
### Local Download
To download the bookcoref data for training and evaluation, run the `download_data.py` script:
```bash
python download_data.py 

options:
  --format <"jsonl" or "conll">, default="jsonl" # Format of the dataset to download.
  --test_only # If specified, only download the test set
  --output_dir <path>, default="data/" # If specified, the output directory for the dataset
```

This script will download data from [🤗 Hugging Face](https://huggingface.co/datasets/sapienzanlp/bookcoref), save it in either JSONL or CoNLL format to the default directory `data/`.

### Data format
BookCoref is a collection of annotated books. Each item contains the annotations of one book following the structure of OntoNotes:

```python
{
  doc_id: "pride_and_prejudice_142", # (str) i.e., id of document 
  sentences: [["Pride", "and", "Prejudice", "."], ["Begin", ...], ...], # list[list[str]] i.e., list of word-tokenized sentences
  clusters: [[[0, 0], [3, 5]],[[4, 9]...], ...], # list[list[list[int]]] i.e., list of clusters' mention offsets
  characters: [
    {
      name: "Mr.Bennet", 
      mentions: [[0, 0], ...],
    },
    {
      name: "Mr. Darcy",
      mentions: [[5, 7], ...],
    }
  ] # list[character], list of characters objects with name and its mentions offsets, i,e., dict[name: str, mentions: list[list[int]]]
}
```

We also include informations on character names, which is not exploited in traditional coreference settings, but could be useful in future work.

## BookCoref Evaluation

To evaluate the outputs of a model on the BookCoref benchmark, run the `evaluate.py` script:

```bash
python scripts/evaluate.py

options:
  --predictions <path_to_predictions> # Path to the predictions file to evaluate.
  --mode <"full", "splitted", "full-window">, default="full" # Evaluation mode.
```

We provide three evaluation modes:

| Mode | Description |
|-------|-------------|
| `full`| Evaluate model predictions on the full books of `test.jsonl`. <br/> *Input*: expects as input predictions on the full test set books. <br/> *Output*: scores on the full books of `test.jsonl`, referred to as BookCoref_gold results in our paper. |
| `splitted` | Evaluate model predictions on `test_splitted.jsonl`. <br/> *Input*: expects as input predictions on the splitted version of our test set books. <br/> *Output*: scores on the splitted version (`test_splitted.jsonl`), referred to as SPLIT-BookCoref_gold results in our paper. |
| `full-window` | Evaluate model predictions carried out on the full `test.jsonl` but evaluated on `test_splitted.jsonl`, by splitting clusters every 1500 tokens. <br/> *Input*: expects as input predictions on the full test set books. <br/> *Output*: scores on the splitted version (`test_splitted.jsonl`), referred to as BookCoref_gold-windows results in our paper. |

## Replicate Paper Results
To replicate the results of our paper, run `scripts/evaluate.py` specifying the path to the predictions of the model you are interested in. 

Example:
```bash
$ python scripts/evaluate.py outputs/longdoc/trained_on_bookcoref/full.jsonl 
> CoNLL-F1: 67.0
```

## Citation
This work has been published at ACL 2025 (main conference). If you use any artifact, please consider citing our paper as follows:

```bibtex
@inproceedings{martinelli-etal-2025-bookcoref,
    title = "{BookCoref}: Coreference Resolution at Book Scale",
    author = "Martinelli, Giuliano  and
      Bonomo, Tommaso  and
      Huguet Cabot, Pere-Llu{\'\i}s  and
      Navigli, Roberto",
    booktitle = "Proceedings of the 63nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
}
```


## License

The data and software are licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

