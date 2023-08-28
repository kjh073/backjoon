n = int(input())
str = ""

for _ in range(n):
	r, s = input().split()
	r = int(r)
	for i in range(len(s)):
		for j in range(r):
			str += s[i]
	print(str)
	str = ""
    