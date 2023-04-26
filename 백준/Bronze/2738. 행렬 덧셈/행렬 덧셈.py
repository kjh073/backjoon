n, m = map(int, input().split())

a = []
b = []
add = []

for _ in range(n):
    add.append([0] * m)

for _ in range(n):
    a.append(list(map(int,input().split()))) 
for _ in range(n):
    b.append(list(map(int,input().split()))) 

for i in range(n):
    for j in range(m):
        add[i][j] = a[i][j] + b[i][j]
        print(add[i][j], end=" ")
    print()
        
