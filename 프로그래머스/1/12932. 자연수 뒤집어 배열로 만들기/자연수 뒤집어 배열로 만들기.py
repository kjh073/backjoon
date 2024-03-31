def solution(n):
    answer = []
    n = str(n)
    for i in range(len(n)):
        answer.append(int(n[i]))
    for i in range(len(n)//2):
        answer[i], answer[len(n) - i - 1] = answer[len(n) - i - 1], answer[i]
    return answer