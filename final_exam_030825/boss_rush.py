
import re

n = int(input())

pattern = r"\|([A-Z]{4,})\|:#([A-Za-z]+ [A-Za-z]+)#"

for _ in range(n):
    line = input()
    match = re.match(pattern, line)
    if match:
        boss = match.group(1)
        title = match.group(2)
        print(f"{boss}, The {title}")
        print(f">> Strength: {len(boss)}")
        print(f">> Armor: {len(title)}")
    else:
        print("Access denied!")



# import re
#
# line_num = int(input())
#
#
#
# for _ in range(line_num):
#     names = input()
#     pattern = r'\|([A-Z]{4,})\|\s*:#([A-Za-z]+) ([A-Za-z]+)#'
#     matches = re.match(pattern, names)
#     name = matches.group(1)
#     title_word_1 = matches.group(2)
#     title_word_2 = matches.group(3)
#     title = title_word_1 + ' ' + title_word_2
#     print(f'{name}, The {title}')
#     print(f'>> Strength: {len(name)}')
#     print(f'>> Armor: {len(title)}')
#     print(f'Access denied!')





