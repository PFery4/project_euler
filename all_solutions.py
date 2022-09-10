"""

This script goes through all solutions.

"""

import glob
import os
from solutions import *

if __name__ == "__main__":
    scripts = sorted(glob.glob('./solutions/*.py'))
    scripts = [os.path.basename(file)[:-3] for file in scripts if os.path.isfile(file) and not file.endswith('__init__.py')]

    for script in scripts:
        print(f"Solution to problem {script[-3:]}:", eval(f"{script}.solution()"))

