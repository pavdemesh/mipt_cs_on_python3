# Determine the longest common subsequence of two lists (arrays)


def lcs(A: list, B: list):
    """
    Returns the length of the longest common subsequence
    """
    # Create convenient variables n and m to store the length of lists
    n = len(A)
    m = len(B)

    # Create a grid size n+1 x m+1 and fill it with zeroes
    F = [[0] * (m + 1) for i in range(n + 1)]

    # Iterate over indices, compare items and update the count of longest subsequence
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Here we use index i-1 and j-1, because A and B are one item shorter then corresponding dimensions of F
            if A[i - 1] == B[j - 1]:
                F[i][j] = 1 + F[i - 1][j - 1]
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])
    for row in F:
        print(row)


seq1 = [2, 4, 6, 10, 15, 8, 9]
seq2 = [1, 7, 2, 5, 4, 6, 11, 15, 8]

lcs(seq1, seq2)
