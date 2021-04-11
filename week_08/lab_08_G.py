def sort_by_ascii(char_sequence):
    """
    Input: A sequence of characters till "." char.
    Convert to ASCII, sort by ASCII codes, convert back to chars.
    Output: Chars sorted by ASCII codes, followed by "."
    """
    # Create new list to store sorted sequence
    sorted_sequence = []

    # Iterate over char_sequence until "." found
    # Convert every item to ASCII and append to new list
    i = 0
    while char_sequence[i] != ".":
        sorted_sequence.append(ord(char_sequence[i]))
        i += 1

    # Sort the list, containing ASCII codes
    sorted_sequence.sort()

    # Iterate over indices of list and convert from ASCII to char
    for i in range(len(sorted_sequence)):
        sorted_sequence[i] = chr(sorted_sequence[i])

    # Append "." at the end of the sorted list
    sorted_sequence.append(".")

    # Print the sorted by ASCII list
    print(*sorted_sequence, sep="")


seq = input()
sort_by_ascii(seq)
