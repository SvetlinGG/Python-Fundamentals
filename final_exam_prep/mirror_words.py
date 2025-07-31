import re
text = input()

arr = []
#pattern = r'([#@]+)([A-Za-z]+)([#@]+)([A-Za-z]+)'
pattern = r'([@#])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'
matches = re.findall(pattern, text)
if matches:
    print(f'{len(matches)} word pairs found!')
else:
    print(f'No word pairs found!')
for match in matches:
    str = match[1]
    sub_str = match[2]
    mirror_str = match[2][::-1]
    if len(str) >= 3 and len(sub_str) >= 3:
        if str == mirror_str:
            arr.append(f'{str} <=> {sub_str}')

if arr:
    print("The mirror words are:")
    print(', '.join(arr))



