from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from logging import getLogger
from warnings import filterwarnings

from .__main__ import main

try:
    from logging import NullHandler
except ImportError:
    from logging import Handler

    class NullHandler(Handler):
        def emit(self, record):
            pass


# Set default logging handler to avoid "No handler found" warnings
getLogger().addHandler(NullHandler())
