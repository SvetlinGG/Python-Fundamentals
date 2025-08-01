username = input()

while True:
    command = input().split(' ')

    if command[0] == 'Registration':
        break
    operation, operation_type = command[0], command[1]
    if command[0] == 'Letters':
        if operation_type == 'Lower':
            print(username.lower())
        elif operation_type == 'Upper':
            print(username.upper())
    if command[0] == 'Reverse':
        start_index, end_index = int(command[1]), int(command[2])
        if 0 <= start_index <= end_index < len(username):
            substring = username[start_index:end_index + 1]
            reversed_substring = substring[::-1]
            username = username[:start_index] + reversed_substring + username[end_index + 1:]
            print(username)
        else:
            continue
    if command[0] == 'Substring':
        substring = command[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")
    if command[0] == 'Replace':
        char = command[1]
        username = username.replace(char, "-")
    if command[0] == 'IsValid':
        char = command[1]
        if char in username:
            print(f'Valid username.')
        else:
            print(f'{char} must be contained in your username.')


