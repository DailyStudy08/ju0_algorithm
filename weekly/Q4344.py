C = int(input())
for i in range(C):
    N = input()
    data = list(map(int, N.split()))
    scores = data[1:]
    avg_score = sum(scores)/data[0]
    over_avg_cnt = 0
    for score in scores:
        if score > avg_score:
            over_avg_cnt +=1
    percent_over_avg = over_avg_cnt / data[0] * 100
    print('%.3f%%' % percent_over_avg)