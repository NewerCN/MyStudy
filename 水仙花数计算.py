def Test(*params,base = 3):
	result = 0
	for each in params:
		result = result + each
		
	result = result * base
	
	print('the result is :',result)

##Test(1,2,3,4,base = 5)

def Narcissistic():
    for each in range(100,1000):
        temp = each
        sum = 0
        while temp:
            sum = sum + (temp%10)**3
            temp = temp//10

        if sum == each:
            print(each,end='\t')

print("所有的水仙花数为：",end=' ')

Narcissistic()
