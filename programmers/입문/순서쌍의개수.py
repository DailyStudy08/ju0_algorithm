def solution(n):
    cnt = 0
    k = int(n ** 0.5)
    if k * k == n:
        cnt -= 1
    for i in range(1, k + 1):
        if n % i == 0:
            cnt += 2
    return cnt