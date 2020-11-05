import argparse


class Parser():

    def parse_args(self):
        """Adding a parser for directory with pictures
        """
        parser = argparse.ArgumentParser()
        parser.add_argument('--path',
                            metavar="path",
                            type=str,
                            required=True,
                            help="path to directory with .JPG files")
        return parser.parse_args()




