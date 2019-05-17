def guess(value):
    guess_me = 7
    if value < guess_me:
        print('too low')

    elif value > guess_me:
        print('too high')
    else:
        print("just right")


guess(4)