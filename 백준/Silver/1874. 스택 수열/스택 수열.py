n = int(input())
i = 1
stack = []
quest = []
q = 0
seq = []

for _ in range(n):
    quest.append(int(input()))
    
while n >= i:
    if len(stack) != 0:
        if stack[len(stack) - 1] == quest[q]:
            stack.pop()
            seq.append('-')
            q += 1
        elif stack[len(stack) - 1] != quest[q]:
            stack.append(i)
            i += 1
            seq.append('+')
    else:
        stack.append(i)
        i += 1
        seq.append('+')

if len(stack) != 0:
    for j in range(len(stack)):
        if stack[len(stack) - 1] == quest[q]:
            stack.pop()
            seq.append('-')
            q += 1
        else:
            break
        
if len(stack) != 0:   
    print('NO')
else:
    for s in seq:
        print(s)