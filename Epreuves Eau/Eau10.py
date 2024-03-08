import sys


if sys.argv[1].isdigit():
    print('Error')
    exit()

STRING = sys.argv[1:]
second_element = STRING[1]
last_element = STRING[-1]

if not STRING:
    print('Error')
    exit()
else:

    for i in range(len(STRING)):
        if last_element == STRING[i]:
            print(i)
            break
        elif second_element == last_element and second_element != STRING[i]:
            print('-1')
            break
    else:
        print("")