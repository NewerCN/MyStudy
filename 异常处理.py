try:
    N = eval(input("请输入一个整数："))
    print(N**2)
except NameError:
    print("输入的不是整数")
