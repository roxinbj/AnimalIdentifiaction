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
    from ..core import ipp
    from cv2 import (
        imread, 
        imshow,
        waitKey,
        destroyAllWindows,
    )
    from multiprocessing.pool import Pool

    from os import listdir, walk
    from os.path import (
        basename,
        dirname,
        exists,
        isdir,
        isfile,
        join,
        relpath,
        splitext,
    )
    from ..common.constant import (
        IMAGE_EXTENTIONS,
    )

    #from ..core import 
    
    #get Input Images
    allowed_input_extentions = [ext.upper() for ext in IMAGE_EXTENTIONS]

    if isdir(input):
        image_filepaths = [
            join(dirpath,filename)
            for dirpath, _, filenames in walk(input)
            for filename in filenames
            if splitext(filename)[1].upper() in allowed_input_extentions
        ]
    else:
        print("No valid directory given")
        return 1

    previous_right_ipp = None
    for index,left in enumerate(image_filepaths):
        right = image_filepaths[
            index +1
            if not index + 1 > len(image_filepaths)
        ] 
        #if right > len(image_filepaths):
        #    print("out of bounce")
        #    break
        
        left_ipp = ipp.ipp(left)
        right_ipp = ipp.ipp(image_filepaths[])
        

        

    # run image preprocessing
    for original in image_filepaths:
        image = ipp.ipp(original)


        imshow('image',image)
        waitKey(0)
        destroyAllWindows()
        print("True")
        
        
    

    print(image_filepaths)


    print("Successfully entered the extract main function!")
    print("End of extract")