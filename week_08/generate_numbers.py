def gen_nums(num_base: int, length: int, prefix=None):
    """
    Will generate all numbers with given num_base of given length
    """
    if length == 0:
        print(prefix)
        return

    prefix = prefix or []

    for digit in range(num_base):
        prefix.append(digit)
        gen_nums(num_base, length - 1, prefix)
        prefix.pop()


gen_nums(3, 2)
