num = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
len_num = len(num)
dial = input()
len_dial = len(dial)
time = []
sum_time = 0

k = 0
for i in range(len(dial)):
    k = 0
    while(k < len_num):
        for j in num[k]:
            if j == dial[len_dial - 1]:
                time.append(k)
                break
        if (len(dial) - len(time) == len_dial - 1):
            len_dial -= 1
            break
        k += 1
    
    
for i in time:
    sum_time += 3
    if i != 0:
        sum_time += i
print(sum_time) 



