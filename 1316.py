# T = int(input())
# cnt = 0

# # 다음 단어와 같으면 pass 아니면 연속되는 것의 마지막 알파벳을 저장
# # 마지막의 경우에는 같아도 저장이 안되고 달라도 저장이 안되기 때문에 따로 저장
# # 연속되던지 안연속되던지 띄엄띄엄 나오면 안되고 1번만 사용되어야 하므로 각 알파벳의 수가 1개여야 한다.
# # 각 단어의 수가 1개인게 아니면 그룹단어 아니다
# # 그룹단어이면 그룹 단어 개수 세어주기
# for tc in range(T):
#     is_group = True
#     s = input()
#     S = len(s)
#     a = []
#     for i in range(S):
#         if i != S - 1 and s[i] != s[i + 1]:
#             a.append(s[i])
#             # print(a)
#         elif i == S - 1:
#             a.append(s[i])
#     for e in a:
#         if a.count(e) != 1:
#             is_group = False
#     if is_group:
#         cnt += 1
#     # print(a)
# print(cnt)

result = 0
for i in range(int(input())):
    word = input()
    # print(word, sorted(word, key=word.find))
    # for i in range(len(word)):
    #     print(word[i], word.find(word[i]))
    # word에 가장 먼저 나왔던 알파벳의 인덱스 위치의 값을 기준으로 단어를 sort해서 순서가 동일하면 그룹문자이지만 뒤에 떨어진 단어가 더 나오면 정렬된 값과 원래 단어가 달라져서 그룹 단어가 안된다.
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)