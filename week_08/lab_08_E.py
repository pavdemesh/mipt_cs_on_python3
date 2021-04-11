def is_correct_sequence(sequence):
    """
    Input: sequence of round brackets
    Output: "Yes" or "No" depending whether the sequence is correct
    """
    stack = 0

    for bracket in sequence:
        if bracket == "(":
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                return "NO"

    return "YES" if stack == 0 else "NO"


seq_from_user = input()
print(is_correct_sequence(seq_from_user))
