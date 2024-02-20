import sys

argument = sys.argv[1:]
mot_inverse = ""

for i in argument:
	mot_inverse += i[::-1] + " "

print(mot_inverse)
