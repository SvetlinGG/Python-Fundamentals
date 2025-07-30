import re
import math

sentence = input()
pattern = r'([:*]{2})([A-Z][a-z]+)\1'
pattern_digits = r'\d'
matches = re.findall(pattern, sentence)
matches_digits = re.findall(pattern_digits, sentence)
digits = [int(d) for d in matches_digits]
multiply_digits = math.prod(digits)
print(f'Cool threshold: {multiply_digits}')
arr = []
newArr = []

for match in matches:
    if len(match[1]) >= 3:
        arr.append(match[1])
        ascii_num = sum([ord(letter) for letter in match[1]])
        if ascii_num >= multiply_digits:
            newArr.append(match)
print(f'{len(arr)} emojis found in the text. The cool ones are:')
for emoji in newArr:
    print(f'{emoji[0]}{emoji[1]}{emoji[0]}')


