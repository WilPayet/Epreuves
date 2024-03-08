import sys

if sys.argv[1].isalpha():
    print('Error')
    exit()


def selection_sort(arr):
    n = len(arr)

    for i in range(n):

        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


my_array = [int(arg) for arg in sys.argv[1:]]

if len(my_array) != len(sys.argv[1:]):
    print('Error')
    exit()


selection_sort(my_array)
print(*my_array)