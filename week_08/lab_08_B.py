def how_many_ones(decimal):
    """
    Given a positive integer, return the number of "1"s in its binary representation
    """
    bin_res = ""
    while decimal > 0:
        bin_res += str(decimal % 2)
        decimal //= 2

    counter = 0
    for digit in bin_res:
        if digit == "1":
            counter += 1

    return counter


print(how_many_ones(int(input())))
