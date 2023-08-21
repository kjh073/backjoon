n, m = map(int, input().split())
bucket = list(range(1, n + 1))

for _ in range(m):
    i, j = map(int, input().split())
    bucket[i - 1], bucket[j - 1] = bucket[j - 1], bucket[i - 1]
    
for i in range(n - 1):
    print(bucket[i], end=" ")
print(bucket[n - 1])