n = int(input())

for _ in range(n):
    strr = input()
    stack = []
    for i in range(len(strr)):
        if strr[i] == '(':
            stack.append(strr[i])
        elif strr[i] == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                stack.append(strr[i])
                break
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')