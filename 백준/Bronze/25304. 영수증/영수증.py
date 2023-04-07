total = int(input())
n = int(input())
sum = 0

for i in range(n):
    money, num = map(int, input().split())
    sum += money * num

if total == sum:
    print("Yes")
else:
    print("No")
