cur_max, last1, last2, last3, last4, last5 = 0, 0, 0, 0, 0, 0

x = int(input())

while x != 0:
    cur_max = max(cur_max, last1)
    last1, last2, last3, last4, last5 = last2, last3, last4, last5, x
    x = int(input())

print(cur_max)
