import logging
import argparse
import sys
import os
from src.services import upload, download
from src import cli

def main():
    logging.root.setLevel(logging.DEBUG)
    args = parse_cmd_args(sys.argv[1:])
    # if verbose flag not passed on as an argument, this will disable all logging levels
    if not args.verbose:
        logging.disable(logging.CRITICAL)  # This will disable all logging

    # if quiet flag is enabled, stdout (console output) is written to devnull where data is discarded
    if args.quiet:
        sys.stdout = open(os.devnull, 'a')

    cli.run(args)

    # identifying if a subparser is invoked. if invoked, call appripriate function
    if 'func' in vars(args):
        print('calling the appropriate function for parser')
        args.func(args)


def parse_cmd_args(cmd_args):
    # create the argument parser
    parser = argparse.ArgumentParser(
        description='A description of the cli program')

    # mutually exclusive means that only one option can be supplied. supplying both will result in an error
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', action='store_true',  # store => true if provided
                       help='Give more output')
    group.add_argument('-q', '--quiet', action='store_true',
                       help='Give no output')

    # # dest='subparser_name' is used to identify the subparser name
    # subparsers = parser.add_subparsers(
    #     title='List of sub commands', description='A description of all the available sub commmands', help='All the commands', dest='subparser_name')

    # # code for subparser command a
    # parser_a = subparsers.add_parser('download', help='help for downloading')
    # parser_a.add_argument('url', type=str, help='url for downloading from')
    # # a function to call when subparser invoked
    # parser_a.set_defaults(func=download.start)

    # # create the parser for the "b" command
    # parser_b = subparsers.add_parser('upload', help='help for uploading')
    # parser_b.add_argument('url', type=str, help='url for uploading to')
    # parser_b.add_argument(
    #     'file', help='file paths. minimum of 1 but can have more', nargs='+')
    # # a function to call when subparser invoked
    # parser_b.set_defaults(func=upload.start)

    # if no arguments are given i.e. only the command name is invoked. this will ensure that the help message is printed out
    if len(cmd_args) == 0:
        parser.print_help()
        sys.exit(1)

    # writing the arguments to a variable to be accesed
    parsed = parser.parse_args(cmd_args)
    return parsed


if __name__ == "__main__":
    main()
