arr =[]
for i in range(2900000):
    if '666' in str(i):
        arr.append(i)
N = int(input())
print(arr[N - 1])
