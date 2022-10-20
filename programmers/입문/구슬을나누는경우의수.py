def solution(balls, share):
    res = 1
    for i in range(balls - share + 1, balls + 1):
        res *= i
    for j in range(1, share + 1):
        res //= j
    return res