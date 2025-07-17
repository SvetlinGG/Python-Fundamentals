import re

names = input()
result = re.findall(r'\b[A-Z][a-z]+ [A-Z][a-z]+\b', names)
print(' '.join(result))