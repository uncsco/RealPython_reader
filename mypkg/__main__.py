"""Read the latest Real Python tutorials.

Usage:
------

    $ realpytho [options] [id] [id ...]

List the latest tutorials:

    $ realpython

Read one tutorial:

    $ realpython <id>

    where <id> is the number shown when listing tutorials.

Read the latest tutorial:

    $ realpython 0


Available options are:

    -h, --help         Show this help
    -l, --show-links   Show links in text


Contact:
--------

- https://realpython.com/contact/

More information is available at:

- https://pypi.org/project/realpython-reader/
- https://github.com/realpython/reader


Version:
--------

- realpython-reader v1.0.0
"""
import sys

#from mypkg import *  #// OKAY
from . import * #// re: __init__.py

def main() -> None:
    """Read the Real Python article feed."""
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    opts = [o for o in sys.argv[1:] if o.startswith("-")]
    print(args)
    print(opts)
    print(hello('Adam'))

    # Show help message
    if "-h" in opts or "--help" in opts:
        print('[--help]')
        raise SystemExit()

if __name__ == '__main__':
    main()
