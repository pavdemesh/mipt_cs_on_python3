N = int(input())
students = []

for i in range(N):
    height, weight = map(float, input().split())
    students.append([height, weight])

students.sort(key=lambda x: x[0], reverse=True)
students.sort(key=lambda x: x[1])

for student in students:

    print("{:.2f} {:.3f}".format(student[0], student[1]))
