N = int(input("请输入一个1-100之间的数: "))
uppower = 1.0
downpower = 1.0

for i in range(365):
    uppower = uppower * (1+N/1000)
    downpower = downpower * (1-N/1000)

a = uppower/downpower

print("{:.2f},{:.2f},{:d}".format(uppower,downpower,int(a)))
