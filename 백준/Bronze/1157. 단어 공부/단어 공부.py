input_str1 = input()
max_cnt = 0
max_char = ''
char = []
cnt = []

str1 = input_str1.upper()
char.append(str1[0])

for i in range(len(str1)):
    if str1[i] not in char:
        char.append(str1[i])

for i in range(len(char)):
    cnt.append(str1.count(char[i]))


if cnt.count(max(cnt)) > 1:
    max_char = '?'
else:
    idx = cnt.index(max(cnt))
    max_char = char[idx]
        
print(max_char)
        