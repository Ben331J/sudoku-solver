from functions import *
from grids import *

grid = rand_select(grids)
print("Original board")
console_display(grid)
grid = solve(grid)
print("Solved grid")
console_display(grid)
