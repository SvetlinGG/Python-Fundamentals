words = input()
reversed_word = ''

for i in range(len(words) -1, -1, -1):
    reversed_word += words[i]
print(reversed_word)