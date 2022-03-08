def board_display(board):
	print(" ---------------------------")
	print("|                           |")
	for x in range(len(board)):
		print("|", end="")
		print(board[x], end="|\n")
		print("|                           |")
		if not (x + 1) % 3:
			print(" ---------------------------")
			if (x + 1) != len(board):
				print("|                           |")
