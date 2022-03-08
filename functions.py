# Display the sudoku board in the console
def board_display(board):

	# For the top of the board
	print(" -----------------------")

	# Print each line of the board
	for x in range(len(board)):

		# Start of the line
		line = "| "

		# Transformation of the line to be displayed with a string
		for y in range(len(board[x])):

			# Add each box in the line
			line += str(board[x][y]) + " "

			# After each third box print a separator
			if not (y + 1) % 3:
				line += "| "

		# Change 0 for white-spaces
		line = line.replace("0", " ")

		# Print the line
		print(line)

		# After each third lines print a separator
		if not (x + 1) % 3:
			print(" -----------------------")
