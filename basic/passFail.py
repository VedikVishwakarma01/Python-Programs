def number(n):
    if n < 35:
        print("you are fail")
    if n > 85:
        print("you get A grade")
    if n > 35 and n < 65:
        print("you get C grade")
    if n < 85 and n > 65:
        print("you get B grade")

n = input("enter your marks:")

number(int(n))

# number(30)
# number(90)
# number(70)



