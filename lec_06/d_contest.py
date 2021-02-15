seq_min = 101
seq_max = 0
running_total = 0
counter = 0
sum_of_mods = 0
current_sum = 0

n = input()

while n != "#":
    try:
        n = int(n)
    except:
        n = list(map(int, n.split()))
        n.append(n[0])
        del n[0]
        print(*n)
        exit()
    running_total += n
    current_sum += n
    counter += 1
    if counter % 3 == 0:
        sum_of_mods += current_sum % n
        current_sum = 0
    seq_max = max(seq_max, n)
    seq_min = min(seq_min, n)
    n = input()

average = round(running_total / counter, 3)

print(average, seq_max, seq_min, sum_of_mods)
