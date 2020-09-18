import WikiHow as wikihow
import argparse

def download():
    # Command line parameters parse
    parser = argparse.ArgumentParser(description='WikiHow Dataset')
    parser.add_argument('--wikihow-dataset-dir',
                        metavar='wikihow_dataset_dir',
                        help='Specify WikiHow Recipes Dataset directory')
    args = parser.parse_args()

    wh = wikihow.WikiHow(args.wikihow_dataset_dir)
    wh.download()



if __name__ == "__main__":
    download()
