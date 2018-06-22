#计算输入数字N的0次方到5次方结果，并依次输出这6个结果，输出结果间用空格分隔
a = input()
b = eval(a)
for i in range(6):
    c = b**i
    i = i+1
    print(c,end=' ')



