import re

destination = input()
pattern = r'([=/])\b([A-Z][a-z]+)([=/])'
#pattern = r"(=|/)([A-Z][a-zA-Z]{2,})\1"
matches = re.findall(pattern, destination)
arr = []
sum = 0

for match in matches:
    start_symbol, word, end_symbol = match[0], match[1], match[2]
    if start_symbol == end_symbol:
        if len(word) >= 3:
            arr.append(word)

print(f"Destinations: {', '.join(arr)}")
for item in arr:
    sum += len(item)
print(f'Travel Points: {sum}')