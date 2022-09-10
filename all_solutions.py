"""

This script goes through all solutions.

"""

import glob
import os
from solutions import *

if __name__ == "__main__":
    scripts = sorted(glob.glob('./solutions/*.py'))
    scripts = [os.path.basename(file)[:-3] for file in scripts if os.path.isfile(file) and not file.endswith('__init__.py')]

    print(scripts)
    print(euler_problem_001.solution())
    print(euler_problem_002.solution())
    for script in scripts:
        #exec('print(f"{script}.solution()")')
        print(eval(f"{script}.solution()"))

