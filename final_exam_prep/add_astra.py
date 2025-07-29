import re

information = input()
pattern = r'([#|])([A-Za-z\s]+)(\1)(\d{2}\/)(\d{2}\/)(\d{2})\1(\d+)\1'
matches = re.findall(pattern, information)
sum_calories = sum([int(calories[3]) for calories in matches])
day_calories = sum_calories // 2000

print(day_calories)