def gen_perm(num_base: int, length: int = -1, prefix=None):
    """
    Will generate all permutations for given range num_base of given length
    """
    length = num_base if length == -1 else length
    prefix = prefix or []

    if length == 0:
        print(*prefix, sep="", end=" / ")
        return

    for digit in range(1, num_base + 1):
        if digit in prefix:
            continue
        prefix.append(digit)
        gen_perm(num_base, length - 1, prefix)
        prefix.pop()


gen_perm(5, 3)
