def even(*n):
    for a in n:
        if a % 2 == 0:
            print(a, "is even number")
        else:
            print(a, "is odd number")


even(3, 4, 5, 6, 7)
even(43, 56, 65, 78, 28)



