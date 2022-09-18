A, B, C = map(int, input().split())
if B >= C and A >= 0:
    print(-1)
else:
    q = A // (C - B) + 1
    print(q)