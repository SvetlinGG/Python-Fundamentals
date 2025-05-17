word = input()

while word != 'End':
    if word != 'SoftUni':
        new_string = ''
        for item in word:
            new_string += item * 2
        print(new_string)
    word = input()