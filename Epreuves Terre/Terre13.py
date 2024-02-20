import sys

trois_entiers = sys.argv[1:]

for i in range(0, len(trois_entiers)):
	for j in range(i+1, len(trois_entier)):
		if trois_entiers[i] >= trois_entiers[j]:
			trois_entiers[i], trois_entiers[j] = trois_entiers[j], trois_entiers[i]

if (sys.argv[1] == sys.argv[2] == sys.argv[3]):
	print("Erreur")
else:
	milieu = len(trois_entiers) // 2
	suisse = trois_entiers[milieu]
	print(suisse)