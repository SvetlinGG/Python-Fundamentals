numbers = input().split(', ')

def is_palindrome(number):

    for digit in numbers:
        if digit == digit[::-1]:
            print('True')
        else:
            print('False')
is_palindrome(numbers)