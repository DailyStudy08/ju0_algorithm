def solution(rsp):
    ans = ''
    for x in rsp:
        if x == '2':
            ans += '0'
        elif x == '0':
            ans += '5'
        else:
            ans += '2'
    return ans