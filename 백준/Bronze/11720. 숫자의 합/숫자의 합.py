num = int(input())
a = input()
sum_n = 0

while num > 0:
    sum_n += int(a[num - 1])
    num -= 1
    
print(sum_n)