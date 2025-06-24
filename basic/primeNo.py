def isPrimeNo(n):
    count = 0
    for a in range(2,n):
        if n % a == 0:
            count = count + 1

    if count > 0:
        print(n, "is not prime no")
    else:
        print(n, "is prime no")


isPrimeNo(13)




