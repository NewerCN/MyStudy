
dayup = 1.0


for i in range(365):
    if i % 5 in [4,0]:
        dayup = dayup*(1-0.01)
    else:
        dayup = dayup*(1+0.01)
        
print("{:.2f}".format(dayup))
