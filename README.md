# wikihow-planning-recipes-dataset

In this repository you will find all necessary scripts to generate the WikiHow Recipes Dataset.

We provide a [file list](./wikihow-recipes-url.txt) of which files comprise our dataset version, in case one wants to reproduce or compare your results over this dataset with other experiments.

### Requirements

We developed all scripts using Python.3.8. The [requirements.txt](./requirements.txt) file lists all required libraries.

### Downloading

Execute ''run.py --wikihow-dataset-dir [destination directory]'' in a shell console. If the destination directory does not exist, the script will try to create it.

### Issues

* If you have network connectivity problems, just re-run the script pointing to the same destination directory, and download will resume from the point where it stopped.

* Articles under WikiHow's quality review will fail to download and an entry will be added to ''error.log'' file. If you want to use the same corpus as us for benchmark purposes, you can download a zip file [here](./wikihow-planning-recipes-data.zip).
