cr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alpha = []

str1 = input()
len_str1 = len(str1)
len_cr = len(cr)
i = 0
j = 0
puls_len = 0

while len_str1 > i:
	j = 0
	while len_cr > j:
		if str1[i] == cr[j][0]:
			if i + 1 < len(str1) and str1[i + 1] == cr[j][1]:
				if cr[j][1] == 'z':
					if i + 2 < len(str1) and str1[i + 2] == '=':
						alpha.append(cr[j])
						puls_len = len(cr[j])
						break
				else:
					alpha.append(cr[j])
					puls_len = len(cr[j])
					break
		j += 1
	if j == len(cr):
		alpha.append(str1[i])
		i += 1
	else:
		i += puls_len

cnt = len(alpha)
print(cnt)