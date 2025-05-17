first_word = input()
second_word = input()

for i in range(len(first_word)):
    if first_word[i] != second_word[i]:
        first_word = second_word[:i + 1] + first_word[i + 1:]
        print(first_word)


