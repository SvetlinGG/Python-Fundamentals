banned_words = input().split(', ')
text = input()

for word in banned_words:

        if len(word) == len(text):
            text = text.replace(word, '*')
            print(text)
