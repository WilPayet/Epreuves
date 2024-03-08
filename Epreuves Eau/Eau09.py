import sys


if len(sys.argv) != 3:
	print('Error')
	exit()

if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
	print('Error')
	exit()

arg = int(sys.argv[1])
arg2 = int(sys.argv[2])

for i in range(arg, arg2):
	print(i, end = ' ')

if (arg > 0 and arg < arg2) or (arg2 > 0 and arg2 < arg):
	ascending = range(arg2, arg)
	for j in ascending:
		print(j, end = ' ')
else:
	print('Error')