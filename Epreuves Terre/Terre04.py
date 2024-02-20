import sys

try:
    a = int(sys.argv[1])
except (IndexError, ValueError):
    print("Tu ne vas pas me la faire !")
    sys.exit(1)

if a % 2 == 0:
    print("pair")
else:
    print("impair")

