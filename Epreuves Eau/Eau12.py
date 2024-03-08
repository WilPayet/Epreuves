import sys

def bubble_sort(array):
	n = len(array)

	swapped = False

	for i in range(n - 1):
		for j in range(0, n - i - 1):
			if array[j] > array[j + 1]:
				swapped = True
				array[j], array[j + 1] = array[j + 1], array[j]
		if not swapped:
			return

array = []

for num in sys.argv[1:]:
	if num.isdigit():
		array.append(int(num))

if len(array) != len(sys.argv[1:]):
	print('Error')
	exit()



bubble_sort(array)

print(*array)