n = 1634
temp = n
r = 0
rn = 0

while temp > 0:
    r = temp % 10
    rn = rn + r*r*r*r
    temp = temp // 10

print(rn )

if n == rn :
    print("this is an armstrong no")
else:
    print("this not an armstrong no")
