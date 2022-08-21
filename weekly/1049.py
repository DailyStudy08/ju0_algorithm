N, M = map(int, input().split())
min_package = 1000
min_each = 1000

for i in range(M):
    p, e = map(int, input().split())
    if p < min_package:
        min_package = p
    if e < min_each:
        min_each = e
if min_package < (min_each * 6):
    case1 = (N // 6 + 1) * min_package 
    case2 = (N // 6) * min_package + (N % 6) * min_each
    price = case1 if case1 < case2 else case2
else:
    price = N * min_each
print(price)