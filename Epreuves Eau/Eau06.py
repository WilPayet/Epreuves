import sys

argument = str(sys.argv[1])

if len(argument) < 2:
    print('Error')
    exit()

for char in argument:
    if char.isnumeric():
        print('Error')
        exit()

index = 0
result = ""

for char in argument:
    if index % 2 == 0 and 'a' <= char <= 'z':
        result += chr(ord(char) - ord('a') + ord('A'))
    else:
        result += char
    index += 1

print(result)
