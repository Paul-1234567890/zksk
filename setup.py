#!/usr/bin/env python
import os
import re

from setuptools import setup


PACKAGE_NAME = "zkbuilder"

INSTALL_REQUIRES = ["petlib", "bplib"]

SETUP_REQUIRES = ["pytest-runner"]

TEST_REQUIRES = ["pytest"]

DEV_REQUIRES = TEST_REQUIRES + ["sphinx", "sphinx_rtd_theme", "m2r", "black"]


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.rst")) as f:
    long_description = f.read()


with open(os.path.join(here, PACKAGE_NAME, "__init__.py")) as f:
    matches = re.findall(r"(__.+__) = \"(.*)\"", f.read())
    for var_name, var_value in matches:
        globals()[var_name] = var_value


setup(
    name=__title__,
    version=__version__,
    description=__description__,
    long_description=long_description,
    author=__author__,
    author_email=__email__,
    packages=["zkbuilder"],
    license=__license__,
    url=__url__,
    install_requires=INSTALL_REQUIRES,
    setup_requires=SETUP_REQUIRES,
    tests_require=TEST_REQUIRES,
    extras_require={"dev": DEV_REQUIRES, "test": TEST_REQUIRES},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Security :: Cryptography",
        "License :: OSI Approved :: MIT License",
    ],
)
