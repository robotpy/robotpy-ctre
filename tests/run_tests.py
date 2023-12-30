#!/usr/bin/env python3

import os
from os.path import abspath, dirname
import sys
import subprocess

if __name__ == "__main__":
    # CTRE's library tends to crash on OSX at program exit, so
    # don't bother running the tests in CI
    if sys.platform != "darwin":
        root = abspath(dirname(__file__))
        os.chdir(root)

        subprocess.check_call([sys.executable, "-m", "pytest"])
