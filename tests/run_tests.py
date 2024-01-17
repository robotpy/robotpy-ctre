#!/usr/bin/env python3

import os
from os.path import abspath, dirname
import sys
import subprocess

if __name__ == "__main__":
    root = abspath(dirname(__file__))
    os.chdir(root)

    try:
        subprocess.check_call([sys.executable, "-m", "pytest"])
    except subprocess.CalledProcessError as e:
        if not (sys.platform == "darwin" and e.returncode == 137):
            raise
