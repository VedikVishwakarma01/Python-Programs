


def noteCounter(amount, *notes):
    for note in notes:
        count = amount // note
        if count > 0:
            print(note, "=", count)
        amount = amount % note


noteCounter(4800, 500,200,100)
noteCounter(7865, 500, 200, 100, 50, 10, 5)