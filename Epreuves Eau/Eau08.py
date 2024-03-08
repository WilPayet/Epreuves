import sys

numbers = sys.argv[1:]

if len(numbers) < 1:
	print('Error')
	exit()


for i in numbers:
	if i.isalpha():
		print('False')
		break
	elif not i.isdigit():
		print('False')
		break
	else:
		True
		print('True')
