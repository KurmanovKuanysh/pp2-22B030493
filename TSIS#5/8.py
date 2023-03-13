import re
new = input('enter: ')
print(re.findall('[A-Z][^A-Z]*', new))