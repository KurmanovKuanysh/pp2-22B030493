import re
new_string = input('enter string: ')
a = re.compile('ab*?')
b = a.search(new_string)

if b:
    print('matches')
else:
    print('no match')