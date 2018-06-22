#LenthExchange.py
#长度转换程序

LengthStr = input()

if LengthStr[-1] == 'm':
    Length = (eval(LengthStr[0:-1])) * 39.37
    print("{:.3f}in".format(Length))

elif LengthStr[-2:] == 'in':
    Length = (eval(LengthStr[0:-2])) / 39.37
    print("{:.3f}m".format(Length))

else:
    print("error!")

