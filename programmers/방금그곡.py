# '''# um =  {'C' : 'a', 'C#': 'b', 'D' : 'c', 'D#': 'd', 'E': 'e', 'F' : 'f', 'F#': 'g', 'G': 'h', 'G#': 'i', 'A' : 'j', 'A#' : 'k', 'B': 'l'}

# def get_ums(melody):
#     ums = []
#     for i in range(len(melody)):
#         if melody[i] == '#':
#             continue
#         if i != len(melody) -1 and melody[i + 1] == '#':
#             ums.append(melody[i:i+2])
#         else:
#             ums.append(melody[i])
#     return ums

# def solution(m, musicinfos):
#     m_ums = get_ums(m)
#     print(m_ums)
#     title_time = []
#     for musicinfo in musicinfos:
#         start, end, title, melody = musicinfo.split(',')
#         # print(start, end, title, melody)
#         end_h, end_m = map(int, end.split(':'))
#         start_h, start_m = map(int, start.split(':')) 
#         m_minus = end_m - start_m
#         h_minus = end_h - start_h
#         tot_m = h_minus * 60 + m_minus
#         # print(tot_m)
#         # print(melody, len(melody))
#         melody_ums = get_ums(melody)
#         melody_ums_len = len(melody_ums)
#         m_q = tot_m // melody_ums_len
#         m_r = tot_m % melody_ums_len
#         final_melody = melody_ums * m_q + melody_ums[ : m_r]
#         print(final_melody, len(final_melody))
        
#         m_str = ''.join(m_ums)
#         melody_str = ''.join(final_melody)
#         print(m_str, melody_str)
#         if m_str in melody_str:
#             print('있다 있어')
#             title_time.append((title, tot_m))
#         # ums = []
#         # for i in range(len(melody)):
#         #     if melody[i] == '#':
#         #         continue
#         #     if i != len(melody) -1 and melody[i + 1] == '#':
#         #         ums.append(melody[i:i+2])
#         #     else:
#         #         ums.append(melody[i])
#         # print(ums)
#         # if m_minus >= 0:
#         #     tot_m = h_minus * 60 + m_minus
#         #     print(tot_m)
#         # else:
#         #     tot_m = (h_minus - 1) * 60 + m_minus + 60
#         #     print(tot_m, '*')
#     print(title_time)
#     tt_cnt = len(title_time)
#     if tt_cnt == 0:
#         ans = "(None)"
#     elif tt_cnt == 1:
#         ans = title_time[0][0]
#     return ans

# print(1)
# print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# # HELLO
# print()
# print(2)
# print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# # FOO
# print()
# print(3)
# print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# # WORLD
# print()
# print(4)
# print(solution("ABC", ["12:34,13:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# # WORLD'''


# def get_ums(melody):
#     ums = []
#     for i in range(len(melody)):
#         if melody[i] == '#':
#             continue
#         if i != len(melody) -1 and melody[i + 1] == '#':
#             ums.append(melody[i:i+2])
#         else:
#             ums.append(melody[i])
#     return ums

# def solution(m, musicinfos):
#     m_ums = get_ums(m)
#     title_time = []
#     for musicinfo in musicinfos:
#         start, end, title, melody = musicinfo.split(',')
#         end_h, end_m = map(int, end.split(':'))
#         start_h, start_m = map(int, start.split(':')) 
#         m_minus = end_m - start_m
#         h_minus = end_h - start_h
#         tot_m = h_minus * 60 + m_minus
#         melody_ums = get_ums(melody)
#         melody_ums_len = len(melody_ums)
#         m_q = tot_m // melody_ums_len
#         m_r = tot_m % melody_ums_len
#         final_melody = melody_ums * m_q + melody_ums[ : m_r] 
#         m_str = '.'.join(m_ums) + '.'
#         melody_str = '.'.join(final_melody) + '.'
#         # print(m_str, melody_str)
#         if m_str in melody_str:
#             title_time.append((title, tot_m))
#     tt_cnt = len(title_time)
#     ans = ''
#     if tt_cnt == 0:
#         ans = "(None)"
#     elif tt_cnt == 1:
#         ans = title_time[0][0]
#     else:
#         maxM = 0
#         for i in range(tt_cnt):
#             if title_time[i][1] > maxM:
#                 ans = title_time[i][0]
#                 maxM = title_time[i][1]
#     return ans

# print(1)
# print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# # HELLO
# print()
# print(2)
# print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# # FOO
# print()
# print(3)
# print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# # WORLD
# print()
# print(4)
# print(solution("ABC", ["12:34,13:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# # WORLD


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
    # elif tt_cnt == 1:
    #     ans = title_time[0][0]
    else:
        maxM = 0
        for i in range(tt_cnt):
            if title_time[i][1] > maxM:
                ans = title_time[i][0]
                maxM = title_time[i][1]
    return ans