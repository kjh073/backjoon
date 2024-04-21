def solution(n):
    strr = ['수', '박']
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += strr[0]
        else:
            answer += strr[1]
    return answer