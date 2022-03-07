import re

def length_check(square):
	input_length = len(square)
	if input_length != 9:
		print("The square must have 9 elements")
		print("You have entered " + str(input_length) + " elements")
		return False
	else:
		return True

print("Welcome to my sudoku resolver")
print("Use only numbers [1-9] and space keys")

square_check = False
while square_check != True:
	square = input("Square : ")

	if length_check(square):
		square_check = True

if square_check == True:
	i = 0
	line_1 = ""
	line_2 = ""
	line_3 = ""
	while i < 3:
		line_1 += square[i]
		i += 1
	while i < 6:
		line_2 += square[i]
		i += 1
	while i < 9:
		line_3 += square[i]
		i += 1

	print("The square is :")
	print(line_1)
	print(line_2)
	print(line_3)