from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import errno
from os import makedirs, remove


def silent_makedirs(path):
    try:
        makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def silent_remove(path):
    try:
        remove(path)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise
