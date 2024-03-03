import math

t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) 
    
    if dist == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if dist > abs(r1 + r2) or dist < abs(r1 - r2):
            print(0)
        elif dist == r1 + r2 or dist == abs(r1 - r2):
            print(1)
        else:
            print(2)