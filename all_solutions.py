"""
This script goes through all solutions.
"""

import glob
import os
import time
from solutions import *


COLWIDTHS = [3, 20, 12]
NA = "N/A"


if __name__ == "__main__":
    
    print("PROJECT EULER SOLUTIONS:\n")
    print(f"{'#'.ljust(COLWIDTHS[0])} | {'SOLUTION'.ljust(COLWIDTHS[1])} | {'TIME [ms]'.ljust(COLWIDTHS[2])}")

    last_problem = int(sorted(glob.glob('./solutions/*.py'))[-1][:-3].split("_")[-1])
    for problem_number in range(1, last_problem + 1):
    	t0 = time.perf_counter_ns()
    	try:
    	    solution = eval(f"euler_problem_{problem_number:03}.solution()")
    	    duration = (time.perf_counter_ns() - t0) / 1e6
    	except:
    	    solution, duration = NA, NA
    	print(f"{str(problem_number).ljust(COLWIDTHS[0])} | "
    	      f"{str(solution).ljust(COLWIDTHS[1])} | "
    	      f"{str(duration).rjust(COLWIDTHS[2])}")

