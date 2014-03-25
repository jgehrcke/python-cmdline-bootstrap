# -*- coding: utf-8 -*-


"""bootstrap: sample command line application"""


from .stuff import Stuff
from .bootstrap import Boo


__version__ = "0.1.0"


def main():
    print("Welcome to '%s', version %s." % (__doc__, __version__))
    print(Stuff)
    print(Boo())


if __name__ == "__main__":
    main()

