subjects = []
sum_grade = 0
cnt_subjects = 0

for _ in range(20):
    subjects.append(list(input().split()))

for i in (subjects):
    # print(i)
    if i[2] == 'A+':
        i.append(4.5)
    elif i[2] == 'A0':
        i.append(4.0)
    elif i[2] == 'B+':
        i.append(3.5)
    elif i[2] == 'B0':
        i.append(3.0)
    elif i[2] == 'C+':
        i.append(2.5)
    elif i[2] == 'C0':
        i.append(2.0)
    elif i[2] == 'D+':
        i.append(1.5)
    elif i[2] == 'D0':
        i.append(1.0)
    elif i[2] == 'F':
        i.append(0.0)

for i in (subjects):
    if i[2] != 'P':
        sum_grade += float(i[1]) * i[3]
        cnt_subjects += float(i[1])
# print(subjects)
if sum_grade == 0:
    print("{:.6f}".format(0))
else:
	print("{:.6f}".format(sum_grade / cnt_subjects))