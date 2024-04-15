def solution(phone_number):
    answer = ''
    idx = len(phone_number) - 1
    
    for i in range(4):
            answer = phone_number[idx - i] + answer
    
    for i in range(idx - 3):
            answer = '*' + answer
        
    return answer