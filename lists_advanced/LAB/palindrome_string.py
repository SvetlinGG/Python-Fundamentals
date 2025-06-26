words = [ str(w) for w  in input().split()]
current_word = input()
count = 0
arr = []

for word in words:

    if word == word[::-1]:
        arr.append(word)
    if word == current_word:
        count += 1
print(arr)
print(f'Found palindrome {count} times')


# words = input().split(' ')
# current_word = input()
# arr = []
# counter = 0
#
# for word in words:
#
#     if word == current_word:
#         counter += 1
#     if word == word[::-1]:
#         arr.append(word)
# print(arr)
# print(f'Found palindrome {counter} times')