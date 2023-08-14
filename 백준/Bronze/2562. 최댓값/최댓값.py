list1 = []
max_num = 0
max_num_seq = 0

for _ in range(9):
    list1.append(int(input()))
    
for i in range(9):
    if list1[i] > max_num:
        max_num = list1[i]
        max_num_seq = i

print(max_num)
print(max_num_seq + 1)