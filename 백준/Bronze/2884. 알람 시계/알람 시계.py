n, m = map(int, input().split())

if m >= 0 and m < 45:
    if n != 0:
        n -= 1
    else:
        n = 23
    tmp = 60 - (45 - m)
    m = tmp
else:
    m -= 45
    
print(n, m)