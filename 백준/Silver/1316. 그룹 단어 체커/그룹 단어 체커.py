n = int(input())
strs = []
cnt = 0

for _ in range(n):
	strs.append(input())

for i in (strs):
	len_str = len(i)
	j = 1
	alpha = []
	while j <= len_str:
		if j != len_str and i[j - 1]!= i[j]:
			if alpha.count(i[j - 1]) == 0:
				alpha.append(i[j - 1])
				j += 1
			else:
				break
		elif j != len_str and i[j - 1]== i[j]:
			j += 1
		elif j == len_str and alpha.count(i[j - 1]) == 0:
				alpha.append(i[j - 1])
				j += 1
		else:
			break
	if j > len_str:
		cnt += 1
# print(strs)
# print(alpha)
print(cnt)