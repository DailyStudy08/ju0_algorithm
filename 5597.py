arr = [0] * 31

for i in range(28):
    n = int(input())
    arr[n] = 1

for j in range(1, 31):
    if arr[j] == 0:
        print(j)
    else:
        continue