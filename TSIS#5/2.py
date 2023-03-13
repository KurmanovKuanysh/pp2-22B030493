import re
new_string = input('enter string : ')
a = re.compile('ab{2,3}?')
b = a.search(new_string)
if b:
    print('match')
else:
    print('not match')