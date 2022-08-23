X = int(input())

for i in range(X):
    s = int(1 + i * (i + 1) / 2)
    e = int((i + 1) * (i + 2) / 2 + 1)
    if s <= X < e:
        if i % 2 == 0:
            res = f'{i + 1 - X + s}/{X - s + 1}'
        else:
            res = f'{X - s + 1}/{i + 1 - X + s}'
        print(res)
        break
