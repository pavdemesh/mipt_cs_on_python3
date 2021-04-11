"""
Input: digit, integer number
Output: How many times digit occurs in number?
"""

digit, number = input().split()
counter = 0

for x in number:
    if x == digit:
        counter += 1

print(counter)
