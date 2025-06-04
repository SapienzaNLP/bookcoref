<div align="center">
  <img src="assets/bookcoref.png" width="700">

</div>

<div align="center">



[![Conference](http://img.shields.io/badge/ACL-2025-4b44ce.svg)](https://20245aclweb.org/)
[![Paper](http://img.shields.io/badge/paper-ACL--anthology-B31B1B.svg)](https://aclanthology.org/)
[![Hugging Face Dataset](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-FCD21D)](https://huggingface.co/collections/sapienzanlp/relik-retrieve-read-and-link-665d9e4a5c3ecba98c1bef19)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-green.svg)](https://opensource.org/licenses/Apache-2.0)
</div>


##  Description
This repository contains the evaluation scripts to evaluate Coreference Resolution models on the BookCoref Benchmark.
We also include the official outputs of the comparison systems, which can be used to reproduce our results.
Our silver training and gold evaluation data can be found on [Hugging Face](https://huggingface.co/datasets/sapienzanlp/bookcoref).
<!-- (we also release wightf of berst performing model bla bla)-->

## 📚 Quickstart

# Setup

1. Clone the repository:
    ```
    git clone https://github.com/Babelscape/cner.git
    ```
2. Create a python environment: 
    ```
    conda create -n env-name python==3.9
    ```
3. Install the requirements:
    ```
    pip install -r requirements.txt
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
