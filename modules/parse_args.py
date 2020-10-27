import argparse


def parse_args():
    """Adding a parser for directory with pictures
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--path',
                        metavar="path",
                        type=str,
                        required=True,
                        help="path to directory with .JPG files")
    return parser.parse_args()


args = parse_args()
folders = args.path

