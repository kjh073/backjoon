chess = [1, 1, 2, 2, 2, 8]

curr = list(map(int, input().split()))
fix = []
for i in range(len(chess)):
    if chess[i] != curr[i]:
        fix.append(chess[i] - curr[i])
    else:
        fix.append(0)

for i in range(len(chess) - 1):
	print(fix[i], end=" ")
print(fix[len(chess) - 1])