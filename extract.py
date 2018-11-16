from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from logging import getLogger

from animal_identification.util.logger import (
    use_multiprocessing_logging,
    init_logging,
    logging_queue,
)
from ..common.constant import (
    DEFAULT_JOBS,
    DEFAULT_OUTPUT_DIRPATH,
    DEFAULT_OUTPUT_FORMAT,
)

LOG = getLogger(__name__)



def main(input,
    yes=True,
    no=True,
    verbosity=0,
):
    print("Successfully entered the extract main function!")
    print("Input is " + input)