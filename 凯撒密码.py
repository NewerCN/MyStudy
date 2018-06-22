P = input()
n = len(P)

for i in range(n):
    x = P[i]
    z = ord(x)
    if x == ' ':
        j = ' '
    else:
        if z < 120:
            m = z+3
        elif z >= 120:
            m = z+3-26
        j = chr(m)
    print(j,end='')
