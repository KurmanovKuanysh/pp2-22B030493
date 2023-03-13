import re
new_string = input('enter string: ')
a = re.compile('a.*?b$')
b = a.search(new_string)

if b:
    print('matches')
else:
    print('not match')