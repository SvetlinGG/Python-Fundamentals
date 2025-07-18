import re

date = input()
pattern = re.compile(r'')

result = re.findall(pattern, date)

for match in result:
    print(match[0])