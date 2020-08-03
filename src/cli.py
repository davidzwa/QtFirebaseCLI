import os
import logging
from src import config_parser

def run(args):
    path = "./QtExampleProject"
    file_traverse(path)
    config_parser.run_parser(path)

def file_traverse(path: str) -> None:
    # dir_path = os.path.dirname(os.path.realpath(path))
    for dirname, dirnames, filenames in os.walk('./QtExampleProject'):
        # print path to all subdirectories first.
        for subdirname in dirnames:
            logging.debug(os.path.join(dirname, subdirname))

        # print path to all filenames.
        for filename in filenames:
            logging.debug(os.path.join(dirname, filename))
