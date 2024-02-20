import sys

try:
	x = int(sys.argv[1])
	y = int(sys.argv[2])
	z = x / y
except ValueError:
	print("On veut un nombre entier !")
except ZeroDivisionError:
	print("On ne divise pas par 0 !")
else:
	a = int(z)
	b = x % y
	print("Resultat:", a)
	print("Reste:", b)

