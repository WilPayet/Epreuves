import sys

arg1, arg2 = str(sys.argv[1]), str(sys.argv[2])

if len(sys.argv) != 3:
        print("Error")
        exit()

if not isinstance(arg2, str):
    print('Error')
else:
    res_first, res_second = arg1[:len(arg1) // 2], arg1[len(arg1) // 2:]

    for char in arg2:
        if not char.isalpha():
            print('Error')
            break
        elif char not in arg1 or arg2.count(char) > arg1.count(char):
            print('False')
            break
    else:
        print('True')
