import re

date = input()
pattern = re.compile(r'\d{2}[./-]\b[A-Za-z]+[-,/]\d{4}')

result = pattern.finditer(date)

for match in result:
    print(match[0])