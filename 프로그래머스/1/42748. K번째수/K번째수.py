def solution(array, commands):
    answer = []
    for com in commands:
        part = array[com[0] - 1:com[1]]
        part.sort()
        answer.append(part[com[2] - 1])
    return answer