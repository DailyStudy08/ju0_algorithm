'''
get_ums를 통해서 C#과 같이 # 이 붙어 있는 경우를 1개의 음으로 인식할 수 있도록 리스트로 바꾼후 다시 join할 때 .을 통해 각 음을 구분할 수 있도록 했습니다. join을 할 때 마지막에 ‘.’을 추가해야합니다. 추가하지 않는다면 ABC가 A.B.C로 되어 A.B.C#인 경우에도 음이 나왔다고 판단할 수 있습니다. 따라서 마지막에도 점을 추가하여 A.B.C.를 만들면 A.B.C#.과 구분이 가능해집니다.

리스트로 분리했다가 다시 join을 사용하는 방법 외에도 방법이 궁금합니다.
'''


def get_ums(melody):
    ums = []
    for i in range(len(melody)):
        if melody[i] == '#':
            continue
        if i != len(melody) -1 and melody[i + 1] == '#':
            ums.append(melody[i:i+2])
        else:
            ums.append(melody[i])
    return ums

def solution(m, musicinfos):
    m_ums = get_ums(m)
    title_time = []
    for musicinfo in musicinfos:
        start, end, title, melody = musicinfo.split(',')
        end_h, end_m = map(int, end.split(':'))
        start_h, start_m = map(int, start.split(':')) 
        tot_m = (end_h - start_h) * 60 + (end_m - start_m)
        melody_ums = get_ums(melody)
        melody_ums_len = len(melody_ums)
        final_melody = melody_ums * (tot_m // melody_ums_len) + melody_ums[ : tot_m % melody_ums_len] 
        m_str = '.'.join(m_ums) + '.'
        melody_str = '.'.join(final_melody) + '.'
        if m_str in melody_str:
            title_time.append((title, tot_m))
    tt_cnt = len(title_time)
    ans = ''
    if tt_cnt == 0:
        ans = "(None)"
    else:
        maxM = 0
        for i in range(tt_cnt):
            if title_time[i][1] > maxM:
                ans = title_time[i][0]
                maxM = title_time[i][1]
    return ans
