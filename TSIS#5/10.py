import re
new = input('enter: ')
str1 = re.sub('(.)([A-Z][a-z]+)' , r'\1_\2' , new)
print(re.sub('([a-z0-9])([A-Z])' , r'\1_\2' , str1).lower())