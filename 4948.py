# while True:
#     n = int(input())
#     if n == 0:
#         break
#     cnt = 0

#     current = n + 1
#     # n + 1 일때 소수가 몇개일까? -> n번의 연산을 함 -> o(n)
#     # current일때 소수의 개수를 k개라고 구했다.
#     next = n + 2
#     # next일때 소수의 개수는 k개로 표현할 수 있다.
#     # next가 소수이면 k + 1 아니면 k개
#     nextOfNext = n + 3
#     # k + 2, k + 1, k
#     # O(2N) -> O(N)

    
#     for x in range(n + 1, 2 * n + 1):
#         if x == 1:
#             continue
#         for i in range(2, x):
#             if x % i == 0:
#                 break
#         else:
#             cnt += 1
#     print(cnt)

# import sys
# input = sys.stdin.readline

# N = 123456*2 + 1
# is_prime = [True] * N

# for i in range(2, int(N**0.5)+1):
#     if is_prime[i]:
#         for j in range(2*i, N, i):
#             is_prime[j] = False

# def cnt(n):
#     cnt = 0
#     for k in range(n + 1, n * 2 + 1):
#         if is_prime[k]:
#             cnt += 1
#     print(cnt)

# while True:
#     k = int(input())

#     if not k:
#         break
#     cnt(k)


# def isprime(n):
#     if n == 1:
#         return False
#     if n == 2 or n == 3:
#         return True
#     if n%2 == 0:
#         return False
#     if n > 3:
#         for i in range(2, int(n**0.5)+1):
#             if n % i == 0:
#                 return False
#     return True
# prime_cnt = [0]
# p_cnt = 0

# for i in range(1, 246913):
#     if isprime(i):
#         p_cnt += 1
#     prime_cnt.append(p_cnt)
    
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     print(prime_cnt[2*n]-prime_cnt[n])

# import sys
# import math

# limit = 123456

# eratos = [1] * (2 * limit + 1)
# eratos[0] = 0
# eratos[1] = 0

# for i in range(2, int(math.sqrt(len(eratos)))):
#     if eratos[i]:
#         for j in range(i + i, len(eratos), i):
#             eratos[j] = 0

# while True:
#     n = int(sys.stdin.readline())

#     if n == 0:
#         break
#     else:
#         print(sum(eratos[n+1:(2*n)+1]))

####################################################

# n = 123456

# table = [0, 0] + [1] * (n * 2 - 1)
# for i in range(2, int((n * 2) ** 0.5) + 1):
#     if table[i]:
#         table[i*2::i] = [0] * ((n * 2) // i - 1)

# while True:
#     n = int(input())
#     if n == 0: 
#         break
#     print(sum(table[n+1:n *2+1]))


