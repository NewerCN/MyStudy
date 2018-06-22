print('******************猜数字******************')
print('*************你只有三次机会哦**************')
temp = input("请猜我想的是哪个数字:")
count = 1
while count <= 3 :   # 次数小于等于3时保持循环
    guess = int(temp)
    if guess == 8:
        print("恭喜你，猜对了")
        break       # 猜对后终止循环
    else:
        if guess > 8:
            print ("哥，大了大了！")
        else:
            print("嘿，小了小了！")
        
    count = count + 1
    
    if count == 4 :     #  三次都没猜对，游戏结束
        print("Sorry，三次都没有猜对，游戏结束！")
        break
    temp = input("哎呀，猜错了，请重新输入吧:")

   
print('****************Game Over****************')
