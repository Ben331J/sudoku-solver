from functions import *
from boards import *

board = rand_select(boards)
print("Original board")
console_display(board)
board = solve(board)
print("Solved board")
console_display(board)
