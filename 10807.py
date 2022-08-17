T = int(input())
a = list(map(int, input().split()))
N = int(input())
cnt = 0
for i in range(T):
    if a[i] == N:
        cnt += 1
print(cnt)