import sys

chiffres = sys.argv[1:]

try:
    chiffres = list(map(int, sys.argv[1:]))
    for i in range(0, len(chiffres)-1):
        if chiffres[i] > chiffres[i+1]:
            print("Pas triée")
            break
    else:
        print("Triée")

except (ValueError):
    print("Erreur: Seuls les nombres entiers sont autorisés")
