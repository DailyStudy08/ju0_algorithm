N = int(input())

for _ in range(N):
    H, W, N = map(int, input().split())
    floor = (N - 1) % H + 1
    ho = (N - 1) // H + 1
    print(f'{floor}{ho:02d}')
