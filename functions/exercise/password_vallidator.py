import string

password = input()
length = len(password)

def password_validator(password):

    allowed = string.ascii_letters + string.digits + " "
    if 6 >= length <= 10:
        print('Password must be between 6 and 10 characters')
    if password[-2:].isalnum():
        print('Password must have at least 2 digits')
    for char in password:
        if char not in allowed:
            print('Password must consist only of letters and digits')


password_validator(password)

# password = input()
# length = len(password)
#
# def password_validator(password):
#     arr = []
#     for char in password:
#         arr.append(char)
#         text = arr[-2:]
#     if 6 >= len(arr) <= 10:
#         print('Password must be between 6 and 10 characters')
#     if char[-2:].isdigit():
#         print('Password must have at least 2 digits')
#     if char.isalnum():
#         print('Password must consist only of letters and digits')
#
# password_validator(password)


