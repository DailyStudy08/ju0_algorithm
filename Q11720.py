N = int(input())
n = input()
digit_str = [*str(n)]
digit_num = list(map(int, digit_str))
digit_sum = sum(digit_num)
print(digit_sum)