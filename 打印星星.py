i = input('请输入一个整数：')
x = int(i)
for n in range(1,x+1):
    a = x -1
    while a :
        print(' ',end='')
        a = a - 1
    b = x
    while b:
        print('*',end='')
        b = b - 1
    print()
    x = x - 1
