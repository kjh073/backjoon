def solution(s):
    answer = ''
    idx = 0
    for i in range(len(s)):
        if s[i].isalpha() == True:
            if idx % 2 == 0:
                answer += s[i].upper()
            else:
                answer += s[i].lower()
            idx += 1
        else:
            answer += s[i]
            idx = 0
    return answer