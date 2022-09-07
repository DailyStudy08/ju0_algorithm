N, M = map(int, input().split())
S = []
for _ in range(N):
    S.append(input().strip())
cnt = 0
for _ in range(M):
    if input() in S:
        cnt += 1
print(cnt)