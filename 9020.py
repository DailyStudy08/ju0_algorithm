N = int(input())

arr = []
for i in range(2, 10000):
    for x in range(2, int(i ** 0.5)+1):
        if i % x == 0:
            break
    else:
        arr.append(i)

for _ in range(N):
    n = int(input())
    m = n // 2
    if m in arr:
        print(f'{m} {m}')
    else:
        a1 = m - 1
        a2 = m + 1
        while True:
            if a1 in arr and a2 in arr:
                print(f'{a1} {a2}')
                break
            else:
                a1 -= 1
                a2 += 1