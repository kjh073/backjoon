def solution(s):
    len_str = len(s)
    if len_str % 2 != 0:
        mid = len_str // 2
        return s[mid]
    else:
        mid = (int)(len_str / 2)
    return s[mid - 1: mid + 1]