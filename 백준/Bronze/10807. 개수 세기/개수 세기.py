n = int(input())
lst = list(map(int, input().split()))
v = int(input())
cnt = 0

for i in lst:
    if v == i:
        cnt += 1
        
print(cnt)