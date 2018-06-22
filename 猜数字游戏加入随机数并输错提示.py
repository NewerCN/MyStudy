import random
secret = random.randint(1,10)
print('******************猜数字******************')
print('*************你只有三次机会哦**************')
temp = input("请猜我想的是哪个数字:")
count = 1
while count <= 3 :
    guess = int(temp)
    
    while type(guess) != type(1):
        print("抱歉，输入的数据不合法,",end='')
        temp = input('请输入一个整数')
        
        if guess == secret:
            print("恭喜你，猜对了")
            break
        else:
            if guess > secret:
                print ("哥，大了大了！")
            else:
                print("嘿，小了小了！")
        count = count + 1

        if count == 4 :     #  三次都没猜对，游戏结束
            print("Sorry，三次都没有猜对，游戏结束！")
            break
        temp = input("哎呀，猜错了，请重新输入吧:")
    
print('****************Game Over****************')

    
