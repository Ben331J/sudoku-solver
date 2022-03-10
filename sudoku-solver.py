import time
from functions import *
from grids import *

grid = rand_select(grids)
print("Original board")
console_display(grid)
start = time.perf_counter_ns()
grid = solve(grid)
stop = time.perf_counter_ns()
time = (stop - start) / 10 ** 6
print(f"Solved grid in {time} ms")
console_display(grid)
