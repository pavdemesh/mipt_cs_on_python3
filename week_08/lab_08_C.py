N = int(input())
answers = list(map(int, input().split()))


def how_many_knights(answers_list: list):
    """
    Gets as input a list of answers right to left and last pointing to first
    And determines how many knights are there guaranteed
    """
    num_of_knights = len(answers_list)
    first_lier = [False] + [bool(x) for x in answers_list[:num_of_knights - 1]]
    first_knight = [True] + [bool(x) for x in answers_list[:num_of_knights - 1]]

    knights_count_first_lier = 0
    knights_count_first_knight = 0

    for i in range(num_of_knights - 1):
        if first_lier[i]:
            continue
        else:
            first_lier[i + 1] = not first_lier[i + 1]

    for k in range(num_of_knights - 1):
        if first_knight[k]:
            continue
        else:
            first_knight[k + 1] = not first_knight[k + 1]

    for is_knight in first_lier:
        if is_knight:
            knights_count_first_lier += 1

    for is_knight in first_knight:
        if is_knight:
            knights_count_first_knight += 1

    return min(knights_count_first_lier, knights_count_first_knight)


print(how_many_knights(answers))
