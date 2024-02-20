import sys


try:
	chiffre_un = int(sys.argv[1])
	chiffre_deux = int(sys.argv[2])
except (ValueError, IndexError):
	print("Ce n'est pas un chiffre")
else:
	if chiffre_un < 0:
		print("Le chiffre doit être positif")
	else:
		c = chiffre_un ** chiffre_deux
		print(c)
