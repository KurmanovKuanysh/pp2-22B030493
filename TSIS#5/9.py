import re
new = input('enter: ')
print(re.sub(r"(\w)([A-Z])" , r"\1 \2",))