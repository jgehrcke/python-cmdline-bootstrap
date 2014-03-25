# -*- coding: utf-8 -*-

import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('bootstrap/bootstrap.py').read(),
    re.M
    ).group(1)

setup(
    name = "cmdline-bootstrap",
    packages = ["bootstrap"],
    entry_points = {
        "console_scripts": ['bootstrap = bootstrap.bootstrap:main']
        },
    version = version,
    description = "Python command line application bare bones template.",
    author = "Jan-Philip Gehrcke",
    author_email = "jgehrcke@googlemail.com",
    url = "http://gehrcke.de/2014/02/distributing-a-python-command-line-application",
    )

