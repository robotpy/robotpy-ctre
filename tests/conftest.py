import os
import sys

if sys.platform == "darwin":
    import atexit

    atexit.register(lambda: os.kill(os.getpid(), 9))
