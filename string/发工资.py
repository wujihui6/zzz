import random

num = 20
money = 10000
for i in range(1,21):
    score = random.randint(1,11)
    if(score < 5):
        continue
    else:
        if(money != 0):
            money = money-1000
            print(money)
        else:
            break
print("工资发完了")