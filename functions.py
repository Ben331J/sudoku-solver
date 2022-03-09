import random



# Select a random board from a list of boards
def rand_select(boards):

	# Random number between 0 and the length of the boards list
	r = random.randrange(0,(len(boards)))
	return boards[r]



# Display the sudoku board in the console
def console_display(board):

	# Print each line of the board
	for y in range(len(board)):

		# Before each group of three lines print a separator
		if not (y) % 3:
			print(" -----------------------")

		# Start of the line
		line = ""

		# Transformation of the line to be displayed with a string
		for x in range(len(board[y])):

			# Before each group of three boxes print a separator
			if not (x) % 3:
				line += "| "

			# Add each box in the line
			line += str(board[y][x]) + " "

		# At the end of the line
		line += "|"

		# Change 0 for white-spaces
		line = line.replace("0", " ")

		# Print the line
		print(line)

	# At the end of the board
	print(" -----------------------")



# Solve a board
def solve(board):

	for y in range(len(board)):

		for x in range(len(board[y])):

			row = board[y]

			column = []
			for i in range(len(board)):
				column.append(board[i][x])

			square = []

			# If the box is empty
			if board[y][x] == '0':

				# Priginal possible numbers
				possible = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

				fo

				# If there is only one possibility
				if len(possible) == 1:
					board[y][x] = possible[0]
		break
