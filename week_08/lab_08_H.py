"""
Compare number in lexicographic order
first by ones, then by tens, then by hundreds etc.
Numbers up to 30.000
"""


def lex_compare_a_b(a: str, b: str):
    """
    Works for numbers in str format of equal length
    Compares from the last digit toward the first digit
    Returns greater number in str format or None if equal
    """
    # Determine length of the number
    size = len(a)

    for k in range(-1, -(size + 1), -1):
        if a[k] > b[k]:
            return a
        elif a[k] < b[k]:
            return b
        else:
            continue
    return None


def quicksort(arr):
    """
    Quicksort using lex_compare_a_b
    Important: Input must be a list of numbers in string format of len 5
    """
    if len(arr) <= 1:
        return
    pivot = arr[0]
    L = []
    M = []
    R = []

    for x in arr:
        if lex_compare_a_b(x, pivot) == pivot:
            L.append(x)
        elif lex_compare_a_b(x, pivot) is None:
            M.append(x)
        else:
            R.append(x)

    quicksort(L)
    quicksort(R)

    k = 0
    for x in L + M + R:
        arr[k] = x
        k += 1


def add_zeros(num: str, length=5):
    """
    Adds non-significant zeros to a number in string format
    Default length to achieve is 5
    """
    if len(num) == length:
        return num
    num = "0" * (length - len(num)) + num
    return num


N = int(input())
numbers_list = input().split()

for i in range(N):
    numbers_list[i] = add_zeros(numbers_list[i])

quicksort(numbers_list)

for i in range(N):
    numbers_list[i] = int(numbers_list[i])

print(*numbers_list, sep=" ")
