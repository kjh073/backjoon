n = int(input())
lst = []

for _ in range(n):
    lst.append(list(map(int, input().split())))
    
for i in range(n):
    sum = lst[i][0] + lst[i][1]
    print(sum)
