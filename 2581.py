M = int(input())
N = int(input())

is_sosu = True
sosu = []
for i in range(M, N + 1):
    for x in range(2, i):
        if i % x == 0:
            is_sosu = False
            break
    else:
        sosu.append(i)
if len(sosu):
    print(sum(sosu))
    print(min(sosu))
else:
    print(-1)
