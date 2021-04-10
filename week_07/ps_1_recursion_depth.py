import sys


def fact(n):
    if n == 0:
        return 1
    return fact(n-1) * n


print(sys.getrecursionlimit())
print(fact(997))
