import math
N, M = map(int, input().split())
x = math.gcd(N,M)
print(x)
print(N * M // x)
