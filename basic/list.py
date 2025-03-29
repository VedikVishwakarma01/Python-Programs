list  = [43, 65, 32, 95, 38, 58, 29]

print(max(list))

print(list)
print("list = ", list)
list1  =["apple", "banana", "cat", "dog", 54, 8895, 54.5654]


j = list1.count(54)
print(j)
print(list1)
print(list1[3])
print(list1[-3])
list1[4] = "horse"
print(list1)

a = list1.index("banana")
print(a)
x, y, z, a, b, c, d = list1
print(x)
print(b)

list2 = list1 + list
print(list2)
list3 = list2*2
print(list3)

s = list1[2:6]
print(s)
k = list1[2:]
print(k)
print(len(list1))

list1.append("cherry")
print(list1)



list1.insert(3, "tiger")
print(list1)
list.remove(95)
print(list)

r = tuple(list1)
print(r)
