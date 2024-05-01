def solution(s):
    flag = True
    for i in s:
        if i.isalpha() == True:
            flag = False
            break
    if flag == True and (len(s) == 4 or len(s) == 6):
        return True
    return False
        
