# find the largest no in list

def higestNo(list):
    b = list[0]
    l = len(list)
    print("length of list = ", l)
    for i in range(l):
        if list[i] > b:
            b = list[i]

    print("Largest no is = ", b)


list = [45, 56, 89,45, 78, 86, 456,90, 34 ]

higestNo(list)

list1 = [56, 78, 89, 90, 45]

higestNo(list1)





