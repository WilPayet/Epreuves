import sys

def fibonacci(term):
    a, b = 0, 1
    for i in range(term + 1):
        a, b = b, a + b
    return a

if len(sys.argv) != 2:
    print(-1)
    exit()

term = sys.argv[1]
if not term.isdigit():
    print(-1)
    exit()

term = int(term)
if term < 0:
    print(-1)
else:
    result = fibonacci(term)
    print(result)
