def is_big(n, p):
    i = 0
    while i < len(p) and n[i] == '0':
        i += 1
    n = n[i:]

    if n == '':
        n = '0'
    if int(n) <= int(p):
        return True
    else:
        return False
    
def solution(t, p):
    answer = 0
    
    for i in range(len(t) - len(p) + 1):
        if is_big(t[i:i + len(p)], p) == True:
            answer += 1
        
    return answer

