from random import random
# import random
a = int(random()*100)
# i = random.randint(1,100)   这两个的意思表达不一致
while True:
    j = int(input("请输入你要猜的数字"))
    if j > a:
        print("太大了")
        continue
    elif j < a:
        print("太小了")
        continue
    else:
        print("猜对了")
        break
        123