from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import logging
from json import load
from logging.config import dictConfig
from multiprocessing import Queue
from os.path import dirname, exists, join, pardir

from contextlib import contextmanager
from threading import Thread

from ..util.os import silent_makedirs


def setup_logging(config_filepath=None, verbosity=0):
    root_dir = join(dirname(__file__), pardir, pardir)
    config_filepath = (
        config_filepath
        if config_filepath
        else join(root_dir, "config", "logging.json")
    )

    """Setup logging configuration"""
    if exists(config_filepath):
        with open(config_filepath, "rt") as config_file:
            config = load(config_file)
        # Init info_file_handler and error_file_handler filename
        filename = config["handlers"]["info_file_handler"]["filename"]
        config["handlers"]["info_file_handler"]["filename"] = filename.format(
            workspaceFolder=root_dir
        )  # , date=datetime.now().strftime('%Y-%m-%d_%H-%M-%S,%f'))
        filename = config["handlers"]["error_file_handler"]["filename"]
        config["handlers"]["error_file_handler"]["filename"] = filename.format(
            workspaceFolder=root_dir
        )  # , date=datetime.now().strftime('%Y-%m-%d_%H-%M-%S,%f'))
        silent_makedirs(join(root_dir, "logs"))
        dictConfig(config)
    else:
        logging.basicConfig()

    if verbosity == 0:
        logging.getLogger().setLevel(logging.INFO)
    else:
        logging.getLogger().setLevel(logging.DEBUG)


# this queue is used to send logging messages from child processes to the main process
logging_queue = Queue(-1)


# copied from "http://plumberjack.blogspot.de/2010/09/using-logging-with-multiprocessing.html"
class QueueHandler(logging.Handler):
    """
    This is a logging handler which sends events to a multiprocessing queue.

    The plan is to add it to Python 3.2, but this can be copy pasted into
    user code for use with earlier Python versions.
    """

    def __init__(self, queue):
        """
        Initialise an instance, using the passed queue.
        """
        logging.Handler.__init__(self)
        self.queue = queue

    def emit(self, record):
        """
        Emit a record.

        Writes the LogRecord to the queue.
        """
        try:
            ei = record.exc_info
            if ei:
                # just to get traceback text into record.exc_text
                dummy = self.format(record)
                record.exc_info = None  # not needed any more
            self.queue.put_nowait(record)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)


@contextmanager
def use_multiprocessing_logging():

    logging_thread = Thread(target=logger_thread)
    logging_thread.start()

    try:
        yield
    finally:
        logging_queue.put_nowait(None)
        logging_thread.join()


def init_logging(q):
    """
    Add a handler to the root logger that pushes all logging messages it gets
    into the logging queue `q`.
    """
    h = QueueHandler(q)
    root = logging.getLogger()
    root.addHandler(h)
    root.setLevel(logging.DEBUG)


def logger_thread():
    while True:
        record = logging_queue.get()
        if record is None:
            break
        logger = logging.getLogger(record.name)
        logger.handle(record)
