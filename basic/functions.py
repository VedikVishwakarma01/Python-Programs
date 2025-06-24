print("------simple function--------")

def sum(a,b):
    c = a + b
    return c
print(sum(5, 10))
print(sum(14, 15))
d = sum(56, 32)
print(d)

def multiply(a, b):
    c = a * b
    return c
print(multiply(23, 65))

print("---------default argument function------------")

def sum (a, b =5):
    c = a + b
    return c
print(sum(10))
print(sum(12, 23))

print("-------------variable argument function--------------")

def sumNum(a, *varg):
    t = 0
    for n in varg:
        print(n)
        t = t + n
    return t

total = sumNum(5,2, 3, 4, 5, 2, 3)
print(total)







