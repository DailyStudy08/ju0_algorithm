import sys
go_to_next_scenario = True
scenario_num = 1

while go_to_next_scenario:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    names = [input() for i in range(n)]
    data_list = [int(sys.stdin.readline().split()[0]) for i in range(2 * n - 1)]
    for i in range(2* n - 1):
        if data_list.count(data_list[i]) == 1:
            exact_num = data_list[i] - 1
            break
    print(f'{scenario_num} {names[exact_num]}')
    scenario_num += 1

# 계속 런타임 에러 났었던 이유 - 인덱스 초과 n인것과 2n-1인것 개수가 다르다는 것을 생각 못함