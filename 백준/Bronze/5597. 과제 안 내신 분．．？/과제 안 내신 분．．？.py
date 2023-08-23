student = list(range(1, 31))

for _ in range(28):
    n = int(input())
    student.pop(student.index(n))

for i in range(2):
    print(student[i])