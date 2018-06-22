N = int(input())
x = int((N+1)/2)

for n in range(1,x+1):
    a = (2*n-1)
    b = a * '*'
    c = b.center(N,' ')
    print(c)
