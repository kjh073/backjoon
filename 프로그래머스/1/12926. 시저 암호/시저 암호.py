def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i].islower() == True:
            answer += chr((ord(s[i]) - ord('a')+ n) % 26 + ord('a'))
        elif s[i].isupper() == True:
            answer += chr((ord(s[i]) - ord('A')+ n) % 26 + ord('A'))
        else:
            answer += s[i]
        
    return answer