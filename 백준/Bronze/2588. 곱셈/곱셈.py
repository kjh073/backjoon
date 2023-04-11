n1 = int(input())
n2 = input()

for i in range(len(n2)):
    n = int(n2[len(n2) - i - 1])
    print(n1 * n)

print(n1 * int(n2))