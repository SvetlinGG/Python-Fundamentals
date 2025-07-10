banned_words = input().split(', ')
text = input()

for word in text.split(' '):
        if word == banned_words[0] or word == banned_words[1]:
            if len(word) == len(banned_words[0]) or len(word) == len(banned_words[1]):
                text = text.replace(word, '*' * len(word))
print(text)


# ban_list = input().split(", ")
# text = input()
#
# replace_symbol = "*"
#
# for ban_word in ban_list:
#     word_len = len(ban_word)
#     text = text.replace(ban_word, f"{word_len * replace_symbol}")
# print(text)
