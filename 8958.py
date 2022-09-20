T = int(input())

for tc in range(T):
    t = input()
    cnt = 0
    score = 0
    for i in range(len(t)):
        if i == 0 and t[i] == 'O':
            cnt = 1
        elif t[i] == 'O' and t[i -1] == t[i]:
            cnt += 1
        elif t[i] == 'O': #
            cnt = 1
        else: 
            cnt = 0
        score += cnt
    print(score)