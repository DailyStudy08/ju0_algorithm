numbers = [0] * 9
for i in range(9):
    numbers[i] = int(input())
maximum = max(numbers)

for i in range(9):
    if maximum == numbers[i]:
        index = i + 1
print(maximum)
print(index)
# 문제가 요구하는 사항 똑바로 보기