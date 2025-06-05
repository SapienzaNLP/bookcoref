<div align="center">
  <img src="https://github.com/tommasobonomo/bookcoref_final/blob/main/assets/bookcoref.png" width="700">

</div>

<div align="center">



[![Conference](http://img.shields.io/badge/ACL-2025-4b44ce.svg)](https://20245aclweb.org/)
[![Paper](http://img.shields.io/badge/paper-ACL--anthology-B31B1B.svg)](https://aclanthology.org/)
[![Hugging Face Dataset](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-FCD21D)](https://huggingface.co/collections/sapienzanlp/relik-retrieve-read-and-link-665d9e4a5c3ecba98c1bef19)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-green.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
</div>


##  Description
This repository contains the official code for "<span style="font-variant: small-caps;">BookCoref</span>: Coreference Resolution at Book Scale".


## Setup 
1. Clone the repository:
    ```
    git clone https://github.com/sapienzanlp/bookcoref.git
    ```
2. Create a python environment: 
    ```
    conda create -n env-name python==3.9
    conda activate env-name
    ```
3. Install the requirements:
    ```
    pip install -r requirements.txt
    ```

## BookCoref Data 
  
### Local Download
  To download the bookcoref data for training and evaluation, use 
  ``` python 
  donwload_data.py 
  args:
    -jsonl # (default) download dataset in jsonlines format.
    -conll # download dataset in conll format
    -test_only # download only testset (for evaluation only)
  ```
  This script will download data from the official repository, that can be found directly on [Huggingface](hf.co/sapienzanlp/bookcoref), in the ``` data/ ``` folder.
  
### Data format
  BookCoref is a collection of annotated books. 
  Each data entry contains information of one book following the traditional structure of OntoNotes:

```python
{
  doc_id: "pride_and_prejudice_142"; # (str) i.e., id of document 
  sentences: [["Pride", "and", "Prejudice", "."], ["Begin", ...], ...]; # list(list(str))) i.e., list of word-tokenized sentences
  clusters: [[[0,0], [3,5]],[[4,9]...], ...]; #llist(list((list(int))) i.e., list of clusters' mention offsets
  characters: [{
    name:"Mr.Bennet", 
    cluster: [[0,0], ...],
    },
    {
      name: "Mr. Darcy",
      cluster: [[5,7], ...],
    }]; #list(character), list of characters objects with name and his mentions offsets, i,e., dict(name:str, cluster:list(list(int)))
}
```

We also include informations on character names, which is not exploited in traditional coreference settings, but can be useful in future works.

## BookCoref Evaluation
use the script ```evaluate.py``` to evaluate model outputs on the bookcoref benchmark.
usage:
```
evaluate.py <path_to_predictions> <mode: "full", "splitted", "full-window", default="full">

```
you can indicate evaluation mode between:

```python
"full" # evaluate models predictions on test.jsonl, expects an input file of predictions on the full testset books. On the paper is referred as BookCoref_gold results.
"splitted" # evaluate model predictions on test_splitted.jsonl, expects an input file of predictions on the split version of our testset books. On the paper is referred as SPLIT-BookCoref_gold results.
"full-window" # evaluate model predictions of the full test.jsonl on test_splitted.jsonl, by splitting clusters every 1500 tokens. Expects an input file of predictions on the full testset books. On the paper is referred as BookCoref_gold-windows.

```
## Replicate Paper Results
use the script ```evaluate.py``` to evaluate model outputs on the bookcoref benchmark.
Example:
```
evaluate.py outputs/longdoc/trained_on_bookcoref/full.jsonl 
---
CoNLL-F1: 67.0
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

