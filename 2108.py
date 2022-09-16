a = []
N = int(input())
for _ in range(N):
    a.append(int(input()))
a.sort()
a1 = sum(a) / N
if a1 - int(a1) >= 0.5:
    a1 = int(a1) + 1
else:
    a1 = int(a1)
print(a1)
a2 = a[N//2]
print(a2)

a_set = set(a)
max_cnt = 0
cnt_lst = []
for e in a_set:
    if a.count(e) >= max_cnt:
        cnt_lst.append(e)
cnt_lst.sort()
a3 = cnt_lst[1]
print(a3)
a4 = max(a) - min(a)
print(a4)