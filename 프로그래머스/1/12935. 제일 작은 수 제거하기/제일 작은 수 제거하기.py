def solution(arr):
    num = min(arr)
    arr.pop(arr.index(num))
    if len(arr) == 0:
        arr.append(-1)
    return arr