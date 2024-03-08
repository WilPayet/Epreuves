import sys


def prime():
	try:
		n = int(sys.argv[1])
		if n <= 0:
			return -1

		next_number = n + 1
		while True:
			for i in range(2, int(next_number/2) + 1):
				if next_number % i == 0:
					break

			else:
				return next_number
			next_number += 1

	except (ValueError, IndexError):
		return -1

resultat = prime()
print(resultat)