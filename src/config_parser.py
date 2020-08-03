import configparser
import logging

# https://docs.python.org/3/library/configparser.html
import os
"""
ConfigParser to parse the right config.ini
Example MyPy https://github.com/python/mypy/blob/master/mypy/config_parser.py
"""
config_header='QtFirebaseCli'
config_file = 'qtfirebase-cli-config.ini'


def run_parser(folder: str) -> str:
    config_file_path = os.path.join(folder, '', config_file)
    logging.debug('config file at' + config_file_path)

    parser = configparser.ConfigParser()
    result = parser.read(config_file_path)
    found_sections = parser.sections()

    for key in parser[config_header]:
        logging.debug([key, parser[config_header][key]])
