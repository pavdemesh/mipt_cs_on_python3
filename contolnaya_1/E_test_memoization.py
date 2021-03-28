def tribonacci(n):
    """ Returns the n-th tribonacci number """
    tribonacci_list = [0, 0, 1]
    if n < len(tribonacci_list):
        return tribonacci_list[n]
    else:
        res = tribonacci(n - 3) + tribonacci(n - 2) + tribonacci(n - 1)
        tribonacci_list.append(res)
        return res


def find_first_larger(x):
    n = 0
    while tribonacci(n) <= x:
        n += 1
    return n


print(find_first_larger(int(input())))
