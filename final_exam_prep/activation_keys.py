
raw_activation_key = input()

command = input().split('>>>')

while command[0] != 'Generate':
    command = input().split('>>>')
    operation, substring = command[0], command[1]
    if operation == 'Contains':

        if substring in raw_activation_key:
            print(f'{raw_activation_key} contains {substring}.')
        else:
            print(f'Substring not found!')
    elif operation == 'Flip':
        operation, letter, start_index, end_index = command[0], command[1], int(command[2]), int(command[3])
        if letter == 'Upper':
            result = raw_activation_key[:start_index] + raw_activation_key[start_index:end_index].upper() + raw_activation_key[end_index:]
            print(result)
        elif letter == 'Lower':
            raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[start_index:end_index].lower() + raw_activation_key[end_index:]
            print(raw_activation_key)
    elif operation == 'Slice':
        operation, start_index, end_index = command[0], int(command[1]), int(command[2])
        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index -1:]
        print(raw_activation_key)

    else:
        print(f'Your activation key is: {raw_activation_key}"')











