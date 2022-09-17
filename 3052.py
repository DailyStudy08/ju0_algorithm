n = [0] * 10

for i in range(10):
    n[i] = (int(input())) % 42
print(len(set(n)))
