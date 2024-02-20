import sys

try:
    argument = str(sys.argv[1])
except (ValueError, IndexError):
    print("Erreur : L'argument n'est pas reconnu.")
else:
    if argument.isdigit():
        print("Erreur: nous ne voulons que des lettres.")
    else:
        taille = 0
        for i in argument:
            taille += 1
        print(taille)
