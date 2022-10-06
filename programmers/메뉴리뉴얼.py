# 오주영

# 문제 풀이
'''
itertools를 사용하여 조합을 만드는 경우의 수를 고려하여 결과값을 리턴하는 문제였다.

course의 각 경우에 대해 order에서 만들 수 있는 조합을 생성하여 알파벳순으로 정렬한 후 문자열로 만들어 문제의 조건에 해당하는 경우 문자열을 answer에 넣을 수 있도록 했다.'''


import itertools

def solution(orders, course):
    answer = []
    for n in course:
        n_dict = {}
        for order in orders:
            if len(order) >= n:
                o_lst = list(order)
                comb = list(itertools.combinations(o_lst, n))
                for c in comb:
                    c = sorted(list(c))
                    s = ''.join(c)
                    n_dict[s] = n_dict.get(s, 0) + 1
        if len(n_dict):
            max_val = max(list(n_dict.values()))
            if max_val >= 2:
                for k, v in n_dict.items():
                    if v == max_val:
                        answer.append(k)
    answer.sort()
    return answer

'''

# 테스트케이스 결과

| 테스트 1 〉 | 통과 (0.12ms, 10.2MB) |
| --- | --- |
| 테스트 2 〉 | 통과 (0.06ms, 10.1MB) |
| 테스트 3 〉 | 통과 (0.11ms, 10.2MB) |
| 테스트 4 〉 | 통과 (0.18ms, 10.2MB) |
| 테스트 5 〉 | 통과 (0.11ms, 10.2MB) |
| 테스트 6 〉 | 통과 (0.58ms, 10.2MB) |
| 테스트 7 〉 | 통과 (0.33ms, 10.2MB) |
| 테스트 8 〉 | 통과 (3.53ms, 10.2MB) |
| 테스트 9 〉 | 통과 (2.41ms, 10.3MB) |
| 테스트 10 〉 | 통과 (2.41ms, 10.6MB) |
| 테스트 11 〉 | 통과 (1.35ms, 10.3MB) |
| 테스트 12 〉 | 통과 (1.58ms, 10.4MB) |
| 테스트 13 〉 | 통과 (2.09ms, 10.4MB) |
| 테스트 14 〉 | 통과 (1.83ms, 10.5MB) |
| 테스트 15 〉 | 통과 (2.20ms, 10.4MB) |
| 테스트 16 〉 | 통과 (0.77ms, 10.4MB) |
| 테스트 17 〉 | 통과 (0.31ms, 10.3MB) |
| 테스트 18 〉 | 통과 (0.15ms, 10.2MB) |
| 테스트 19 〉 | 통과 (0.02ms, 10.2MB) |
| 테스트 20 〉 | 통과 (0.41ms, 10.2MB) |
'''