"""

This script goes through all solutions.

"""

import glob
import os
import time
from solutions import *

if __name__ == "__main__":
    scripts = sorted(glob.glob('./solutions/*.py'))
    scripts = [os.path.basename(file)[:-3] for file in scripts if os.path.isfile(file) and not file.endswith('__init__.py')]


    print("PROJECT EULER SOLUTION SPOILERS:\n")

    colwidths = [10, 20, 10]
    print(f"{'#'.ljust(colwidths[0])}|{'SOLUTION'.ljust(colwidths[1])}|{'TIME [ms]'.ljust(colwidths[2])}")

    for script in scripts:
        
        time_0 = time.perf_counter_ns()
        solution = eval(f"{script}.solution()")
        duration = (time.perf_counter_ns() - time_0) / 1e6
        print(f"{script[-3:].ljust(colwidths[0])}|{str(solution).ljust(colwidths[1])}|{str(duration).rjust(12)}")

