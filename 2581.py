M = int(input())
N = int(input())


sosu = []
for i in range(M, N + 1):
    is_sosu = True
    if i == 1:
        is_sosu = False
    for x in range(2, i):
        if i % x == 0:
            is_sosu = False
            break
    if is_sosu:
        sosu.append(i)
if len(sosu):
    print(sum(sosu))
    print(min(sosu))
else:
    print(-1)
