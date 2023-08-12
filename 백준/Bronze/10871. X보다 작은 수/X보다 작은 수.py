n, x = map(int, input().split())
list1 = list(map(int, input().split()))

for i in range(n):
    if list1[i] < x:
        print(list1[i])