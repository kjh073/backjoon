def solution(s):
    answer = 0
    sign = 1
    if s[0] == '+':
        s = s[1:]
    elif s[0] == '-':
        sign *= -1
        s = s[1:]
    s = int(s)
    answer = sign * s
    return answer