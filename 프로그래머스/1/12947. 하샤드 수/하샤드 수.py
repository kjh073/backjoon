def sum_of_num(n):
    result = 0
    while n != 0:
        result += n % 10
        n = n // 10
    return result
        

def solution(x):
    n_sum = sum_of_num(x)
    if x % n_sum == 0:
        answer = True
    else: 
        answer = False
    return answer