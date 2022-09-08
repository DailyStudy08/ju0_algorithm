N = int(input())
n = N
i = 2
while n > 0:
    while n % i == 0:
        print(i)
        n /= i
    if n == 1:
        break
    i += 1