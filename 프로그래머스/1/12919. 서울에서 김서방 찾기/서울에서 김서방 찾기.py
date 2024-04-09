def solution(seoul):
    loc = 0
    for text in seoul:
        if text == 'Kim':
            break
        loc += 1
    answer = '김서방은 ' + str(loc) + '에 있다'
    return answer