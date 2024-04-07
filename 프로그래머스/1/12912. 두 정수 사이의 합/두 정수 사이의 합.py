def solution(a, b):
    if a > b:
        a, b = b, a
    num = (b + a) / 2
    reap = b - a + 1

    answer = num * reap
    return answer