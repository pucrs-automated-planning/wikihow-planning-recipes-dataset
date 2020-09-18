# wikihow-planning-recipes-dataset

In this repository you will find all necessary scripts to generate WikiHow Recipes Dataset.

We provide a [file list](./wikihow_recipes_url.txt) of which files compose our dataset version, in case you want to reproduce or compare your results over this dataset with other experiments.

### Requirements

This script is developed in Python.3.8. We suggest that you verify [requirements.txt](./requirements.txt) file for required libraries.

### Downloading

Execute ''run.py --wikihow-dataset-dir [destination directory]'' in a shell console. If the destination directory does not exist, the script will try to create it.

### Issues

* If you have network connectivity problems, just re-run the script pointing to the same destination directory, and download will resume from the point where it stopped.

* Articles under WikiHow's quality review will fail to download and an entry will be added to ''error.log'' file. If you want to use the same corpus as us for benchmark purposes, you can download a zip file [here](./wikihow-planning-recipes-data.zip).
