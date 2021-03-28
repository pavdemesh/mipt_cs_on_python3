def dot_product(n, vector_1, vector_2):
    scalar_product = 0
    for index in range(n):
        scalar_product += vector_1[index] * vector_2[index]
    return scalar_product


print(dot_product(3, [1, 2, 3], [1, 2, 3]))
print(dot_product(3, [1, 2, 3], [4, 5, 6]))