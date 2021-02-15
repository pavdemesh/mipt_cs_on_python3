def define_triangle_type():
    sides = list()
    for _ in range(3):
        sides.append(int(input()))

    sides.sort(reverse=True)

    longest = sides[0]
    side_1 = sides[1]
    side_2 = sides[2]

    if longest >= side_2 + side_1:
        return "impossible"

    if longest ** 2 == side_1 ** 2 + side_2 ** 2:
        return "right"

    if longest ** 2 > side_1 ** 2 + side_2 ** 2:
        return "obtuse"

    if longest ** 2 < side_1 ** 2 + side_2 ** 2:
        return "acute"


print(define_triangle_type())
