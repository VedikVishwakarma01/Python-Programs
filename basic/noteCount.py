notes = (500, 200, 100, 50, 20, 10,)
amount = 4900
count = 0

for note in notes:
    count = amount // note
    if count > 0:
        print(note, "=", count)
    amount = amount % note





