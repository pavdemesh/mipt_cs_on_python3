def tribonacci(n):
    """ Returns the n-th tribonacci number """
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1

    a, b, c = 0, 0, 1
    for i in range(n-2):
        x = a + b + c
        a, b, c = b, c, x
    return x


def find_first_larger(x):
    n = 0
    while tribonacci(n) <= x:
        n += 1
    return n


print(find_first_larger(int(input())))
