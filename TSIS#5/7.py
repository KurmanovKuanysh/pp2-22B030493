import re
new = input('enter: ')
print(''.join(x.capitalize() or '_' for x in new.split('_')))
