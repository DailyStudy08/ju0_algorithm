s = input()
s_len = len(s)
for i in range(s_len - 2):
    for j in range(i, s_len - 1):
        for k in range(j, s_len):
            a = s[i:-1:-1]
            print(i)
            b = s[j:i - 1:-1]
            c = s[k -1: j:-1:-1]
            print(a, b, c)
            print(s[i:j])