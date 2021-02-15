my_text = input()
my_power = int(input())


def string_root(text, power):
    power = -power

    if power > len(text) or len(text) % power != 0:
        return "NO SOLUTION"

    step = len(text) // power
    slicing = text[: step]

    for k in range(0, len(text) - step + 1, step):
        if slicing != text[k: k + step]:
            return "NO SOLUTION"
    return slicing


if my_power > 0:
    print(my_text * my_power)
else:
    print(string_root(my_text, my_power))
