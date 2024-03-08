import sys

if len(sys.argv) <= 1:
    print('Error')
    exit()

if sys.argv[1].isalpha():
    print('Error')
    exit()

arguments = sys.argv[1:]
array = []
results = []

for arg in arguments:
    array.append(int(arg))

for i in range(len(array) - 1):
    for j in range(i + 1, len(array)):

        result = abs(array[j] - array[i])
        results.append(result)


minimum_absolute = min(results)

print(minimum_absolute)