a = list(map(int, input().split()))
asc = True
des = True
for i in range(1, 8):
    if a[0] == 1:
        des = False
        if a[i] != a[i - 1] + 1 :
            asc = False
            print('mixed')
            break
    elif a[0] == 8:
        asc = False
        if a[i] != a[i - 1] - 1 :
            des = False
            print('mixed')
            break
    else:
        print('mixed')
        break
else:
    if asc:
        print('ascending')
    elif des:
        print('descending')