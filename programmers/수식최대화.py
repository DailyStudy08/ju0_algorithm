from itertools import permutations


def calc(a1, a2, p):
    if p == '+':
        return (a1 + a2)
    elif p == '-':
        return (a1 - a2)
    elif p == '*':
        return (a1 * a2)


def solution(expression):
    x = 0
    s = []
    c = []
    for i in range(len(expression)):
        if not expression[i].isdigit():
            c.append(expression[i])
            s.append(expression[x:i])
            s.append(expression[i])
            x = i + 1
    s.append(expression[x:])
    c_lst = list(set(c))
    k = list(permutations(c_lst, len(c_lst)))
    s2 = s[:]
    answer = 0
    for sunseo in k:
        s2 = s[:]
        stack = []
        if len(sunseo) == 1:
            p1 = sunseo[0]
            while s2:
                tmp = s2.pop(0)
                if tmp.isdigit() or (len(tmp) > 1 and '-' in tmp):
                    stack.append(tmp)
                else:
                    if tmp == p1:
                        a1 = int(stack.pop())
                        a2 = int(s2.pop(0))
                        res = calc(a1, a2, p1)
                        stack.append(res)
                    else:
                        stack.append(tmp)
            ans = abs(stack[0])
            if ans > answer:
                answer = ans
        elif len(sunseo) == 2:
            p1 = sunseo[0]
            p2 = sunseo[1]
            while s2:
                tmp = s2.pop(0)
                if tmp.isdigit() or (len(tmp) > 1 and '-' in tmp):
                    stack.append(tmp)
                else:
                    if tmp == p1:
                        a1 = int(stack.pop())
                        a2 = int(s2.pop(0))
                        res = calc(a1, a2, p1)
                        stack.append(res)
                    else:
                        stack.append(tmp)
            stack2 = []
            while stack:
                tmp = str(stack.pop(0))
                if tmp.isdigit() or (len(tmp) > 1 and '-' in tmp):
                    stack2.append(tmp)
                else:
                    a1 = int(stack2.pop())
                    a2 = int(stack.pop(0))
                    res = calc(a1, a2, p2)
                    stack2.append(res)
            ans = abs(stack2[0])
            if ans > answer:
                answer = ans
        else:
            p1 = sunseo[0]
            p2 = sunseo[1]
            p3 = sunseo[2]
            while s2:
                tmp = s2.pop(0)
                if tmp.isdigit() or (len(tmp) > 1 and '-' in tmp):
                    stack.append(tmp)
                else:
                    if tmp == p1:
                        a1 = int(stack.pop())
                        a2 = int(s2.pop(0))
                        res = calc(a1, a2, p1)
                        stack.append(res)
                    else:
                        stack.append(tmp)
            stack2 = []
            while stack:
                tmp = str(stack.pop(0))
                if tmp.isdigit() or (len(tmp) > 1 and '-' in tmp):
                    stack2.append(tmp)
                else:
                    if tmp == p2:
                        a1 = int(stack2.pop())
                        a2 = int(stack.pop(0))
                        res = calc(a1, a2, p2)
                        stack2.append(res)
                    else:
                        stack2.append(tmp)
            stack3 = []
            while stack2:
                tmp = str(stack2.pop(0))
                if tmp.isdigit() or (len(tmp) > 1 and '-' in tmp):
                    stack3.append(tmp)
                else:
                    a1 = int(stack3.pop())
                    a2 = int(stack2.pop(0))
                    res = calc(a1, a2, p3)
                    stack3.append(res)
            ans = abs(stack3[0])
            if ans > answer:
                answer = ans
    return answer
