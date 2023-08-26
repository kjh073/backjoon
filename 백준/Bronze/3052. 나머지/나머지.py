nums = []
cnt = 1

for _ in range(10):
    nums.append(int(input())%42)
nums.sort()
    
for i in range(9):
    if nums[i] != nums[i + 1]:
        cnt += 1
        
print(cnt)