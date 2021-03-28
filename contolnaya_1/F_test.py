num1 = int(input())
num2 = int(input())


def highest_common_divisor(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return highest_common_divisor(a % b, b)


print(highest_common_divisor(num1, num2))
