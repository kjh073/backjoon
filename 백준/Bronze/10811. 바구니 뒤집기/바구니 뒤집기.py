n, m = map(int, input().split())
bucket = list(range(n + 1))
    
for _ in range(m):
	i, j = map(int, input().split())
	while i <= j:
		bucket[i], bucket[j] = bucket[j], bucket[i]
		i += 1
		j -= 1

for i in range(1, n):
    print(bucket[i], end=" ")
print(bucket[n])