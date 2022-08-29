N = int(input())
if N % 5 == 0:
    print(N // 5)
else:
    q1 = N // 5
    r1 = N - 5 * q1
    if r1 % 5 == 0:
        print(q1 + r1 // 3)
    elif r1 % 5 == 1:
        if q1 >= 1:
            q2 = (r1 + 5) // 3
            print(q1 - 1 + q2)
        else:
            print(-1)
    elif r1 % 5 == 2:
        if q1 >= 2:
            q2 = (r1 + 5 * 2) // 3
            print(q1 - 2 + q2)
        else:
            print(-1)
    elif r1 % 5 == 3:
        print(q1 + r1 // 3)
    elif r1 % 5 == 4:
        if q1 >= 1:
            q2 = (r1 + 5) // 3
            print(q1 - 1 + q2)
        else:
            print(-1)
    else:
        print(-1)