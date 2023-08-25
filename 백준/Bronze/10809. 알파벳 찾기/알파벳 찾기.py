s = input()
char = ord('a')

for _ in range(25):
    if s.find(chr(char)) != -1:
        print(s.find(chr(char)), end=" ")
    else:
        print(-1, end=" ")
    char += 1
if s.find(chr(char)) != -1:
	print(s.find(chr(char)))
else:
	print(-1)