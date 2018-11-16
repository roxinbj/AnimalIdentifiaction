import sys
from argparse import ArgumentParser
from logging import getLogger
from os.path import relpath

from .__version__ import __version__
from .api import extract
from .common import constant
from .util.logger import setup_logging

try:
    from inspect import getfullargspec
except ImportError:
    # Python 2 backward compatibility
    from inspect import getargspec as getfullargspec

LOG = getLogger(__name__)

def main(argv=None):
    args = _args(argv)
    
    setup_logging(verbosity=args.verbosity)
    command = args.command
    args = vars(args)
    spec = getfullargspec(command)
    #print("Str: " + str(args.input))
    try: 
        if not spec.varkw:
            #No kwarks, remove unexpected arguments.
            args = {key: args[key] for key in args if key in spec.args}
    except AttributeError:
        # Python 2 backward compatibility
        if not spec.keywords:
            # No kwargs, remove unexpected arguments.
            args = {key: args[key] for key in args if key in spec.args}
    try:
        LOG.debug("Executing command ... ")
        LOG.debug(args)
        command(**args)
        LOG.debug("Successful execution")
    except RuntimeError as err:
        LOG.critical(err)
        return 1
    return 0

def _args(argv=None):
    # create parser with options common to all parsers
    commonParser = ArgumentParser(add_help=False)
    commonParser.add_argument(
        "-v",
        dest="verbosity",
        action="count",
        default=0,
        help="verbosity of the logging",
    )

    #create main parser
    parser = ArgumentParser("farm-watch", parents=[commonParser])
    parser.set_defaults(command=parser.print_help)
    parser.add_argument(
        "--version",
        action="version",
        version=__version__,
        help="Print version and exit",
    )

    #create subcommand parsers
    subparsers = parser.add_subparsers()
    _extract_cmd(subparsers,commonParser)

    # PArse argumnets
    args = parser.parse_args(argv)

    return args

def _extract_cmd(subparsers,commonParser):
    parser = subparsers.add_parser(
        "extract",
        parents=[commonParser],
        description="This will be the description of the animal identifiaction",
        help="helo of animal identification",
    )    
    parser.set_defaults(command=extract.main)

    parser.add_argument(
        "input",
        help="Input data to be analysed. Can be folder or file",
    )

    parser.add_argument(
        '-o',
        "--output",
        default=constant.DEFAULT_OUTPUT_DIRPATH,
        help="output directory (default: {}".format
            (relpath(constant.DEFAULT_OUTPUT_DIRPATH)
        ),
    )
    
if __name__=="__main__":
    try:
        status = main()
    except:
        LOG.critical("Shutting down due to fatal error")
        raise # print stack trace
    else:
        raise SystemExit(status)


        