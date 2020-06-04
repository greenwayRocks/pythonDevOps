import re
name = ''
while not re.fullmatch('[a-z]{3,}', name.lower()):
    print('What is your name? ', end='')
    name = input()
print('done!')

