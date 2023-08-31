n = int(input())

for i in range(1, n * 2):
    if i <= n:
        for j in range(n - i):
            print(" ",end="")
        for j in range(2 * i - 1):
            print("*",end="")
        print()
    else:
        for j in range(i - n):
            print(" ",end="")
        for j in range((n * 2 - i ) * 2 - 1):
            print("*",end="")
        print()