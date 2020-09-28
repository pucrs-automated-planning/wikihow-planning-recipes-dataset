# WikiHow Planning recipes Dataset

[![DOI](https://zenodo.org/badge/294817862.svg)](https://zenodo.org/badge/latestdoi/294817862)


In this repository you will find all necessary scripts to generate the WikiHow Recipes Dataset. We used this dataset to evaluate our work published in the [KEPS@ICAPS 2020 Workshop](https://icaps20subpages.icaps-conference.org/workshops/keps/) entitled **Planning Domain Generation from Natural Language Step-by-Step Instructions**.

We provide a [file list](./wikihow-recipes-url.txt) of which files comprise our dataset version, in case one wants to reproduce or compare your results over this dataset with other experiments.

### Requirements

We developed all scripts using Python.3.8. The [requirements.txt](./requirements.txt) file lists all required libraries.

### Downloading

Execute ''run.py --wikihow-dataset-dir [destination directory]'' in a shell console. If the destination directory does not exist, the script will try to create it.

### Publication

If you find this dataset useful, please cite our paper:

> STEINERT, Maurício; and MENEGUZZI, Felipe. Planning Domain Generation from Natural Language Step-by-Step Instructions. In 2020 Workshop on Knowledge Engineering for Planning and Scheduling (KEPS@ICAPS), Nancy, France, 2020.

```Bibtex
@inproceedings{Steinert2020,
author = {Maur\'{i}cio Steinert and Felipe Meneguzzi},
title = {{Planning Domain Generation from Natural Language Step-by-Step Instructions}},
booktitle = {Proceedings of the 2020 Workshop on Knowledge Engineering for Planning and Scheduling (KEPS@ICAPS)},
year = {2020}
}
```

### Issues

* If you have network connectivity problems, just re-run the script pointing to the same destination directory, and download will resume from the point where it stopped.

* Articles under WikiHow's quality review will fail to download and an entry will be added to ''error.log'' file. If you want to use the same corpus as us for benchmark purposes, you can download a zip file [here](./wikihow-planning-recipes-data.zip).
