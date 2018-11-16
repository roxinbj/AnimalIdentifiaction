from os.path import dirname, join, pardir

ROOT_DIRPATH = join(dirname(__file__),pardir,pardir)

# Global definitions
IMAGE_EXTENTIONS = [".jpg", ".jpeg",".png" ]
OUTPUT_EXTENSIONS = [".jpg", ".jpeg",".png" ]

# Global Default Settings
DEFAULT_OUTPUT_EXTENSION = ".jpg"
DEFAULT_JOBS = 4
DEFAULT_OUTPUT_DIRPATH = join(
    ROOT_DIRPATH,
    "data",
    "result",
    "{input_dirname}",
    "{animal_name}",
    "{input_filename}" + "{input_extension}",
)

# CLI/API specific default settings
VALID_OUTPUT_FORMATS = [ext[1:] for ext in OUTPUT_EXTENSIONS]
DEFAULT_OUTPUT_FORMAT = DEFAULT_OUTPUT_EXTENSION[1:]
