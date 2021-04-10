def gen_bin(length:int, prefix=""):
    """
    Will generate all binary numbers of given length
    """
    if length == 0:
        print(prefix)
        return

    gen_bin(length - 1, prefix + "0")
    gen_bin(length - 1, prefix + "1")


gen_bin(4)
