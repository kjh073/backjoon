str_list = []

while True:
    s = input()
    if s == '.':
        break
    str_list.append(s)
   

for strr in str_list:
    stack = []
    for i in range(len(strr)):
        if strr[i] == '(' or strr[i] == ')' or strr[i] == '[' or strr[i] == ']':
            if strr[i] == '(' or strr[i] == '[':
                stack.append(strr[i])
            elif strr[i] == ')' or strr[i] == ']':
                if len(stack) != 0 and stack[len(stack) - 1] == '(' and strr[i] == ')':
                    stack.pop()
                elif len(stack) != 0 and stack[len(stack) - 1] == '[' and strr[i] == ']':
                    stack.pop()
                else:
                    stack.append(strr[i])
                    break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')