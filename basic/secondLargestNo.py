def secondLargest(list):

    first = list[0]
    second = 0

    l = len(list)

    print("length of list =", l)

    for i in range(l):
        if list[i] > first :
            second = first
            first = list[i]
        if list[i] < first and list[i] > second :
            second = list[i]


    print("Second largest no is =", second)

list = [54, 78, 23, 44, 90, 58, 28]
secondLargest(list)
