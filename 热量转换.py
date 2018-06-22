a = input()

if a[-1] == 'J':
    b = (eval(a[0:-1])) / 4.186
    print("{:.3f}cal".format(b))

elif a[-3:] == 'cal':
    b = (eval(a[0:-3])) * 4.186
    print("{:.3f}J".format(b))

else:
    print("input error")
