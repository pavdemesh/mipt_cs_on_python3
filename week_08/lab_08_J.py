"""
Input: int N followed by N latin words on N separate lines
Output: Sorted by length, with printed length on separate line AND
Reversed word followed by original word sorted by reversed word lexicographically
"""

N = int(input())
latin_words = list()
# Get  latin words and append to list
for i in range(N):
    word = input()
    latin_words.append(word)

# Sort first by reversed word ascending
latin_words.sort(key=lambda x: x[::-1])

# Sort by word length ascending
latin_words.sort(key=len)

# Create list to keep track of already printed word lengths
printed_nums = list()

# Iterate over words, print length if not already printed
# Print reversed word followed by original word
for word in latin_words:
    if len(word) not in printed_nums:
        print(len(word))
        printed_nums.append(len(word))
    # print("{} {}".format(word[::-1], word))
    print(f"{word[::-1]} {word}")
