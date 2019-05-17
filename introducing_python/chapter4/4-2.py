guess_me = 7
start = 1

while start <= guess_me:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it!')
        break
    else:
        print('oops')
    start += 1