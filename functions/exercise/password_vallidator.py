password = input()
length = len(password)

def password_validator(password):
    arr = []
    for char in password:
        arr.append(char)
        text = arr[-2:]
    if 6 >= len(arr) <= 10:
        print('Password must be between 6 and 10 characters')
    if char[-2:].isdigit():
        print('Password must have at least 2 digits')
    if char.isalnum():
        print('Password must consist only of letters and digits')

password_validator(password)


