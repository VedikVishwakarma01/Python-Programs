num = [34, 56, 78, 90, 75, 32]

first = second = float('-inf')

for n in num:
    if n > first:
        second = first
        first = n

    if n > second and n != first:
        second = n

print("second largest:", second)







