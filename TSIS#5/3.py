import re
new_string = input('enter sring: ')
a = re.compile('[a-z]+_[a-z]+')
b = a.search(new_string)
if b:
    print("matches")
else:
    print('not match')