curr = input()

if curr[:3] == 'RMB':
    ex = eval(curr[3:])/6.78
    print("USD{:.2f}".format(ex))

elif curr[0:3] == 'USD':
    ex = eval(curr[3:])*6.78
    print("RMB{:.2f}".format(ex))
