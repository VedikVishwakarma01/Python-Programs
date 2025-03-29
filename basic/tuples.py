# Tuple is like list but tuple are immutable, elements in it cannot be changed

t = (43, 78, 98, 64, 72, 90)
print(t)
print(t[1])
print(t[5])
print(len(t))
s= t[2:4]
print(s)
j = t[2:]
print(j)


t1 = ("apple", "banana", "cat", "dog", "elephant", "horse")

t3= t+ t1
print(t3)
t4= t1*2
print(t4)

r = list(t)
print(r)