total = int(input())
n = int(input())
lst = []
sum = 0

for _ in range(n):
    lst.append(list(map(int, input().split())))
    
for i in range(n):
    sum += lst[i][0] * lst[i][1]

if total == sum:
    print("Yes")
else:
    print("No")
