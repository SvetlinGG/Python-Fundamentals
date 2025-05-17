num_of_strings = int(input())

for words in range(num_of_strings):
    words = input()
    if ',' in words or '.' in words or '_' in words:
        print(f"{words} is not pure!")
    else:
        print(f'{words} is pure.')