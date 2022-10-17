def solution(record):
    inout = []
    id_name = {}
    for r in record:
        lst = r.split()
        if len(lst) == 3:
            p, idx, name = r.split()
            id_name[idx] = name
        else:
            p, idx = r.split()
        inout.append((idx, p))
    answer = []
    for el in inout:
        if el[1] == 'Enter':
            answer.append(f'{id_name[el[0]]}님이 들어왔습니다.')
        elif el[1] == 'Leave':
            answer.append(f'{id_name[el[0]]}님이 나갔습니다.')
    return answer