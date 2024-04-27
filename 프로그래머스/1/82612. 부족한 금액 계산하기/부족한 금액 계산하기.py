def solution(price, money, count):
    need = 0
    for i in range(count):
        need += price * (i + 1)
    if money - need >= 0:
        return 0
    else:
        return abs(money - need)
