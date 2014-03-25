# -*- coding: utf-8 -*-


"""bootstrap.bootstrap: provides entry point main()."""


__version__ = "0.2.0"


from .stuff import Stuff


def main():
    print("Executing bootstrap version %s." % __version__)
    print(Stuff)
    print(Boo())


class Boo(Stuff):
    pass
