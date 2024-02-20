import sys

n = int(sys.argv[1])
premier = True

for i in range(2, int(n / 2) + 1):
  if (n % i) == 0:
    premier = False
    break

if premier:
    print("Vrai", (n), "est un nombre premier.")
else:
    print("faux", (n), "n'est pas un nombre premier.")
