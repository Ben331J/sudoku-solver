import random
import copy



# Select a random grid from a list of grids
def rand_select(grids):

	# Random number between 0 and the length of the grids list
	r = random.randrange(0,(len(grids)))
	return grids[r]



# Display the sudoku grid in the console
def console_display(grid):

	# Print each line of the grid
	for y in range(len(grid)):

		# Before each group of three lines print a separator
		if not (y) % 3:
			print(" -----------------------")

		# Start of the line
		line = ""

		# Transformation of the line to be displayed with a string
		for x in range(len(grid[y])):

			# Before each group of three boxes print a separator
			if not (x) % 3:
				line += "| "

			# Add each box in the line
			line += str(grid[y][x]) + " "

		# At the end of the line
		line += "|"

		# Change 0 for white-spaces
		line = line.replace("0", " ")

		# Print the line
		print(line)

	# At the end of the grid
	print(" -----------------------")



# Solve a grid
def solve(grid):

	solving_grid = copy.deepcopy(grid)

	for y in range(len(solving_grid)):

		for x in range(len(solving_grid[y])):

			row = solving_grid[y]

			column = []
			for c in range(len(solving_grid)):
				column.append(solving_grid[c][x])

			square = []
			s_y0 = (y // 3) * 3
			s_x0 = (x // 3) * 3
			for s_y in range(3):
				for s_x in range(3):
					square.append(solving_grid[s_y0 + s_y][s_x0 + s_x])

			# If the box is empty
			if solving_grid[y][x] == 0:

				# Priginal possible numbers
				possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]

				for n in range(1, 10):
					if n in row or n in column or n in square:
						possible.remove(n)

				# If there is only one possibility
				if len(possible) == 1:
					solving_grid[y][x] = possible[0]
	
	if solving_grid != grid:
		solve(solving_grid)
	
	return solving_grid
