
list_of_chars = input().split(', ')

chars = {}
for char in list_of_chars:
    chars[char] = ord(char)
print(chars)