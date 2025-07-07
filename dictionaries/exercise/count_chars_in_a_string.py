
words = input().replace(' ', '')

count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

for key, value in count.items():
    print(f'{key} -> {value}')
