now_hour, now_min = map(int, input().split())
cook_time = int(input())
cook_hour = cook_time // 60
cook_min = cook_time % 60
now_hour = (now_hour + cook_hour + (now_min + cook_min)//60) % 24
now_min = (now_min + cook_min) % 60
print(now_hour, now_min)