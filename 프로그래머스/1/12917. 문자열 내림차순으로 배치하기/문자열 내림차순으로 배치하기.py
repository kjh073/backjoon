def qsort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    low = []
    high = []
    for value in arr[1:]:
        if value > pivot:
            low.append(value)
        else:
            high.append(value)
    return qsort(low) + [pivot] + qsort(high)


def solution(s):
    answer = ''
    cupper = []
    clower = []
    sortupper = []
    sortlower = []
    
    for c in s:
        if c.isupper() == True:
            cupper.append(c)
        else:
            clower.append(c)
            
    sortupper = qsort(cupper)
    sortlower = qsort(clower)
    
    for c in sortlower:
        answer += c
    for c in sortupper:
        answer += c
            
    return answer