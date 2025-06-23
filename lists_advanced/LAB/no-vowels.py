
word = input()
vowels = ['a', 'o', 'e', 'i', 'u', 'A','I', 'U','E', 'O']

result = [str(letter) for letter in word if letter not in vowels]
print(''.join(result))




#word = input()
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#
# def is_vowel(word):
#
#     for char in word:
#         if char in vowels:
#             word = word.replace(char, '')
#     print(word)
#
# is_vowel(word)