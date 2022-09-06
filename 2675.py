T = int(input())

for tc in range(T):
    n, s = input().split()
    n = int(n)
    ans = ''
    for i in range(len(s)):
       ans += s[i] * n
    print(ans)
    
# 각각 공백으로 구분된 것이 문자와 숫자가 섞여있으면 자료형 변환 똑바로 했는지 확인할 것