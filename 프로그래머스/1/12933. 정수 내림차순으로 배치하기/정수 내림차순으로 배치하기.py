def solution(n):
    num = []
    answer = 0
    while n != 0:
        num.append(n % 10)
        n = n // 10 
        print(n)
    num.sort(reverse = True)
    print(num)
    for i in range(len(num)):
        answer *= 10
        answer += num[i]
    print(answer)
    return answer