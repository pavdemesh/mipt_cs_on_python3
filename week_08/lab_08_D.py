"""
Input: price, (daily) delta, m: num of weeks
Output: how much money in total spent after m weeks
"""

price, delta, m = map(int, input().split())
day = 1
money = 0

while day <= m * 7:
    money += price
    price += delta
    day += 1

print(money)
