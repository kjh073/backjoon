nums = []
max_num = 0
max_row = 0
max_col = 0
for _ in range(9):
    nums.append(list(map(int, input().split())))
    
# print(nums)

for i in range(9):
    for j in range(9):
        if max_num < nums[i][j]:
            max_num = nums[i][j]
            max_row = i
            max_col = j
            
print(max_num)
print(max_row + 1, max_col + 1)