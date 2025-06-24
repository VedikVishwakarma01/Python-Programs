def odd(*n):
    count = 0
    for a in n:
        for i in range(2, a):
            if a % i == 0:
                count = count + 1

        if count > 0:
            print(a, "is not a prime no")
            count = 0
        else:
            print(a, "is a prime no")



odd(2, 3, 4, 5, 6, 7, 8, 9)

