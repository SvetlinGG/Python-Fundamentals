
count = int(input())

word_synonyms = {}

for _ in range(count):
    word = input()
    synonym = input()
    word_synonyms[word] = word_synonyms.get(word, []) + [synonym]

for word in word_synonyms:
    print(f'{word} - {", ".join(word_synonyms[word])}')