dices = list(map(int, input().split()))

dices_len = len(dices)
same = 1
num = 0
price = 0
for i in range(dices_len):
    for j in range(i + 1, dices_len):
        if dices[i] == dices[j]:
            same += 1
            num = dices[i]


if same == 4:
    same -= 1
if same == 3:
    price = 10000 + num * 1000
elif same == 2:
    price = 1000 + num * 100
elif same == 1:
    price = max(dices) * 100
    
print(price)
    