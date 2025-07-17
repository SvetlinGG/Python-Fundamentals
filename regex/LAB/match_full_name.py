import re

names = input()
result = re.findall(r'\b[A-Z]', names)
print(result)