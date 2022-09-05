# 11:49
N = int(input())
n_lst = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if n_lst[i] == 1:
        continue
    for x in range(2, n_lst[i]):
        if n_lst[i] % x == 0:
            break
    else:
        cnt += 1

print(cnt)