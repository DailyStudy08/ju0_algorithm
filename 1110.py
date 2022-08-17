N = int(input())

cnt = 0
calc = N

while True:
    if calc < 10:
        calc = (calc % 10) * 10 + (calc // 10 + calc % 10) % 10
    else:
        calc = (calc % 10) * 10 + (calc // 10 + calc % 10) % 10
    cnt += 1
    if calc == N:
        break
print(cnt)
