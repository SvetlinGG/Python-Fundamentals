import re

sentence = input()
pattern = r'([:*]{2})([A-Z][a-z]+)\1'
matches = re.findall(pattern, sentence)

for match in matches:
    if len(match[1]) >= 3:
        print(match[1])