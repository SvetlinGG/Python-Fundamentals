banned_words = input().split(', ')
text = input()

for word in text.split(' '):
        if word == banned_words[0] or word == banned_words[1]:
            if len(word) == len(banned_words[0]) or len(word) == len(banned_words[1]):
                text = text.replace(word, '*')
print(text)
