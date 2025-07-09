# word = input()
# second_word = input()
#
# result = second_word.replace(word, '')
# print(result.replace(word, ''))

first_string = input()
second_string = input()

while first_string in second_string:
    second_string = second_string.replace(first_string, '')
print(second_string)