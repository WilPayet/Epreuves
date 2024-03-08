import sys

argument = str(sys.argv[1])


if argument.isdigit():
	print("Error")
	exit()

new_arg = ""
First_letter = True

for char in argument:
	if char.isalpha():
		if First_letter == True:
			new_arg += chr(ord(char) - ord('a') + ord('A'))
			First_letter = False
		else:
			new_arg += char
	else:
		new_arg += char
		First_letter = True

print(new_arg)