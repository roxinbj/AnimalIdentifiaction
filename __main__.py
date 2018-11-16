from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)


def main():
    from . import cli

    status = cli.main()
    return status

if __name__=="__main__":
    raise SystemExit(main())