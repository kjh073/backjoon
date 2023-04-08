n = int(input())
lst = list(map(int, input().split()))

max = max(lst)

for i in range(len(lst)):
        lst[i] = lst[i] / max * 100

avg = sum(lst) / len(lst)
print(avg)