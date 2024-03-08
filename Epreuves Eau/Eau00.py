import sys

if len(sys.argv) == 1:
    numbers_combination = []

    for raw1 in range(0, 10):
        for raw2 in range(0, 10):
            for raw3 in range(0, 10):
                if raw1 < raw2 < raw3:
                    if (raw1 == raw2 and raw1 == raw3) or (raw1 != raw2) or (raw2 != raw3) or (raw1 != raw3):
                        numbers_combination.append(f"{raw1} {raw2} {raw3}")

    print(', '.join(numbers_combination))
else:
    print("Veuillez ne rien écrire s'il vous plaît!")
