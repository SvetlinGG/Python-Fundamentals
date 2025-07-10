
single_str = input()
digits = []
letters = []
others = []

for letter in single_str:
    if letter.isdigit():
        digits.append(letter)
    elif letter.isalpha():
        letters.append(letter)
    else:
        others.append(letter)
print(''.join(digits))
print(''.join(letters))
print(''.join(others))