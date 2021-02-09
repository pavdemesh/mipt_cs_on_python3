# Eratosthenes sieve
N = 100
arr = [True] * N
arr[0] = arr[1] = True
for k in range(2, N):
    if arr[k]:
        for m in range(k+k, N, k):
            arr[m] = False

for i in range(N):
    print(i, "-->", "simple" if arr[i] else "complex")

