thinkers = ['Plato', 'PlayDo', 'Gumby']

while True:
    try:
        thinker = thinkers.pop()
        print(thinker)
    except IndexError as err:
        print('We tried to pop too many thinkers!')
        print(err)
        break

print('Done...')
