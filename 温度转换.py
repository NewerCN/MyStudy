TempStr = input()
if TempStr[0] == 'F':
    C = (eval(TempStr[1:])-32)/1.8
    print("转换成摄氏温度的温度为C{:.2f}".format(C))


elif TempStr[0] == 'C':
    F = eval(TempStr[1:])*1.8+32
    print("转换成华氏温度的温度为F{:.2f}".format(F))


else :
    print("输入有误！")
