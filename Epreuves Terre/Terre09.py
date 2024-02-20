import sys

try:
	a = int(sys.argv[1])
	b = a ** 0.5
except (ValueError, IndexError):
	print("seuls les nombres entiers positifs sont autorisés")
else:
	print("la racine carée de", (a), "est:", (round(b)))