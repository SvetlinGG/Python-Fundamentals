char_one = input()
char_two = input()

def two_characters(char_one, char_two):

    num_one = ord(char_one)
    num_two = ord(char_two)


    for num in range(num_one + 1, num_two):

        print(chr(num), end=' ')
two_characters(char_one, char_two)