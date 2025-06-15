words = input().split(' ')
current_word = input()
arr = []
counter = 0

for word in words:

    if word == current_word:
        counter += 1
    if word == word[::-1]:
        arr.append(word)
print(arr)
print(f'Found palindrome {counter} times')