word = input()
vowels = ['a', 'e', 'i', 'o', 'u']

def is_vowel(word):

    for char in word:
        if char in vowels:
            word = word.replace(char, '')
    print(word)

is_vowel(word)