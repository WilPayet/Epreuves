import sys

if len(sys.argv) == 1:
	combo = []

	for i in range(0, 100):
		for j in range(0, 100):
			two_digit = f"{i:02d} {j:02d}"
			if i < j:

				combo.append(two_digit)

	print(', '.join(combo))
else:
	print('erreur')