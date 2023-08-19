n, m = map(int, input().split())
bucket = []
for i in range(n + 1):
    bucket.append(0) 
    
for _ in range(m):
	a, b, c = map(int, input().split())
	for i in range(a, b + 1):
		bucket[i] = c
   
for i in range(1, n):
    print(bucket[i], end=" ")
print(bucket[n])