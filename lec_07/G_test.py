""" Highest frequency of an int in sequence using just list functionality """

sequence = [0] * 100

counter = int(input())

for _ in range(counter):
    x = int(input())
    sequence[x] += 1

max_frequency = 0
position_number = 0

for k in range(100):
    if sequence[k] > max_frequency:
        max_frequency = sequence[k]
        position_number = k

print(position_number)
