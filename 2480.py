dice = list(map(int, input().split()))
if dice[0] == dice[1] and dice[0]== dice[2]:
    print(10000 + dice[0] * 1000)
elif dice[0] == dice[1]:
    print(1000 + dice[1] * 100)
elif dice[0]== dice[2]:
    print(1000 + dice[0] * 100)
elif dice[1] == dice[2]:
    print(1000 + dice[1] * 100)
else:
    dice_max = 0
    for i in range(3):
        if dice_max < dice[i]:
            dice_max = dice[i]
    print(dice_max * 100)
