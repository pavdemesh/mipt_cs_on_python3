N = 50
arr = [True] * N

for k in range(2, N):
    if arr[k]:
        for m in range(k+k, N, k):
            print(f"m is now {m}")
            arr[m] = False

for i in range(N):
    print(i, "-", "simple" if arr[i] else "complex")
