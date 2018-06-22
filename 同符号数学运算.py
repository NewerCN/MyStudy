N = int(input())
a = abs(N)
b = a + 10
c = a - 10
d = a * 10
if N < -10:
  b = -b
  c = -c
  d = -d
elif N >= 0 and N <10:
  b = b
  c = abs(c)
  d = d
elif N > -10 and N < 0:
  b = -b
  c = c
  d = -d
else:
  b = b
  c = c 
  d = d
print(a,b,c,d)
