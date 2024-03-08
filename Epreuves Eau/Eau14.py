import sys

if sys.argv[1].isnumeric():
    print('Error')
    exit()

my_list = sys.argv[1:]

n = len(my_list)

for i in range(n - 1):
    for j in range(0, n - i - 1):
        elem1 = my_list[j]
        elem2 = my_list[j + 1]
        ascii_order1 = tuple(map(ord, elem1))
        ascii_order2 = tuple(map(ord, elem2))

        if ascii_order1 > ascii_order2:
            my_list[j] = elem2
            my_list[j + 1] = elem1

if len(my_list) != len(sys.argv[1:]):
    print('Error')
    exit()


print(' '.join(my_list))
