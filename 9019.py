from collections import deque
import sys
input = sys.stdin.readline
def bfs(N, M):
    q = deque()
    v = set()
    q.append((N, ''))
    v.add(N)
    while q:
        n, s = q.popleft()
        if n == M:
            print(s)
        for i in ['D', 'S', 'L', 'R']:
            if i == 'D':
                ne = (2 * n) 
                if ne > 9999:
                    ne %= 10000
            elif i == 'S':
                ne = 9999 if n == 0 else n - 1
            elif i == 'L':
                ne = n % 1000 * 10 + n // 1000

            elif i == 'R':
                ne = n % 10 * 1000 + n // 10

            if not ne in v:
                v.add(ne)
                q.append((ne, s + i))

T =  int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    bfs(N, M)