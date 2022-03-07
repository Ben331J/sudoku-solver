# This program will resolve a sudoku

# Module importation
import re



# Function to verify if the user input has 9 digit or space
# Return true if it's correct or false if not
def regex_verify(square):
	regex = r"^[\d\s]{9}$"

	if re.search(regex, square):
		return True

	else:
		print("The square must have 9 digits or white-spaces")
		return False



# Program start
print("Welcome to my sudoku resolver")


main_input_list = ("N", "E")

user_input = ""

while user_input not in main_input_list:
	print("Press N to enter a new square")
	print("Press E to exit")
	user_input = input("? : ")

if user_input == "N":
	print("Use only digits [1-9] and white-spaces to enter a new square")

	# Ask user for square input
	square_correct = False

	# Input verify
	while square_correct != True:
		
		original_square = input("Original square : ")
		
		if regex_verify(original_square):
			square_correct = True

	# If the user input is correct
	# The original square is displayed
	if square_correct == True:
		
		count = 0
		line_count = 0
		box_count = 0
		line = ""
		lines = []

		while line_count < 3:
			line += original_square[box_count]
			count += 1
			box_count += 1

			if count == 3:
				lines.append(line)
				count = 0
				line_count += 1
				line = ""

		# Display the square
		print("The square is :")
		for x in lines:
			print(x)

	resolve_input_list = ("R", "E")

	input("Press R to resolve :")

if user_input == "E":
	print("Bye")
