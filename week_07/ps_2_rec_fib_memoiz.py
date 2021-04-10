# Cache to store intermediary results
fib_cache = {1: 1, 2: 1}


def rec_fib(n):
    if n in fib_cache:
        return fib_cache[n]
    fib_num = rec_fib(n-1) + rec_fib(n-2)
    fib_cache[n] = fib_num
    return fib_num


print(rec_fib(236))
