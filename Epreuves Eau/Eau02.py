import sys

if len(sys.argv) >= 2:
    argument_array = sys.argv[1:]

    for word in argument_array[::-1]:
        print(f'"{word}"')
else:
    print("Erreur : Veuillez entrer au moins 2 arguments.")
    exit()
