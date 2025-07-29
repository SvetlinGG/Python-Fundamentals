import re

information = input()
pattern = r"(?i)([#|])([a-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
matches = re.findall(pattern, information)
sum_calories = sum([int(calories[3]) for calories in matches])
days = sum_calories // 2000
print(f'You have food to last you for: {days} days!')
for item in matches:
    print(f'Item: {item[1]}, Best before: {item[2]}, Nutrition: {item[3]}')