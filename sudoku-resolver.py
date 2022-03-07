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

# Function to display a square
# It take a 9 digits or white-space in parameter
def square_display(square):
	count = 0
	line_count = 0
	box_count = 0
	line = ""
	lines = []

	while line_count < 3:
		line += square[box_count]
		count += 1
		box_count += 1

		if count == 3:
			lines.append(line)
			count = 0
			line_count += 1
			line = ""

	# Display the square
	for x in lines:
		print(x)

# Function to verify if the square is complete
# Return true or false
def square_is_complete(square):
	regex = r"^[\d]{9}$"

	if re.search(regex, square):
		return True

	else:
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
		print("The square is :")
		square_display(original_square)

	resolve_input_list = ("R", "E")
	user_input = ""

	while user_input not in resolve_input_list:
		print("Press R to resolve")
		print("Press E to exit")
		user_input = input("? : ")

		if user_input == "R":

			square = original_square
			possible_digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

			for x in square:
				if x in possible_digits:
					possible_digits.remove(str(x))

			while not square_is_complete(square):
				square = re.sub(r"\s", possible_digits[0],square, 1)
				del possible_digits[0]

			# Result display
			square_display(square)


		elif user_input == "E":
			print("Bye")

elif user_input == "E":
	print("Bye")
