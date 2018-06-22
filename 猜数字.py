print('------------我爱Python-------------')
temp = input("不妨猜一下东哥现在心里想的是哪个数字:")
guess = int(temp)
while guess != 8 :
    guess = int(temp)
    if guess == 8:
        print("恭喜你，猜对了")
    else:
        if guess > 8:
            print ("哥，大了大了！")
        else:
            print("嘿，小了小了！")
        temp = input("哎呀，猜错了，请重新输入吧:")
print("游戏结束，不玩啦~")
        

    
