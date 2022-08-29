S = input()

tot = 0
for i in range(len(S)):
    if S[i] in 'ABC':
        tot +=  3
    elif S[i] in 'DEF':
        tot +=  4
    elif S[i] in 'GHI':
        tot +=  5
    elif S[i] in 'JKL':
        tot +=  6
    elif S[i] in 'MNO':
        tot +=  7
    elif S[i] in 'PQRS':
        tot +=  8
    elif S[i] in 'TUV':
        tot +=  9
    elif S[i] in 'WXYZ':
        tot +=  10
    elif S[i] in '1':
        tot +=  2
    elif S[i] in '0':
        tot +=  11
print(tot)