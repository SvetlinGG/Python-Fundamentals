import re

phone = input()
pattern = re.compile(r'\+359([ -])2\1([0-9]{3})\1([0-9]{3})\d')
list_result = list()
result = re.finditer(pattern, phone)
for match in result:
    list_result.append(match[0])

print(*list_result, sep=', ')
