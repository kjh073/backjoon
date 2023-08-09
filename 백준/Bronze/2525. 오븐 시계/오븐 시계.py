h, m = map(int, input().split())
n = int(input())
tmp = 0

if 60 - m < n:
    tmp += n - (60 - m)
    h += tmp // 60 + 1
    m += tmp % 60 + n - tmp
else:
    m += n
    if m >= 60:
        h += 1
if m >= 60:
    m -= 60
if h >= 24:
    h -= 24   
    
print(h, m)