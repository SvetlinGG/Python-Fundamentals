
raw_activation_key = input()

command = input().split('>>>')

while command[0] != 'Generate':

    if operation == 'Contains':
        operation, substring = command[0], command[1]
        if substring in raw_activation_key:
            print(f'{raw_activation_key} contains {substring}.')
        else:
            print(f'Substring not found!')
    elif operation == 'Flip':
        operation, letter, start_index, end_index = command[0], command[1], command[2], command[3]
        if letter == 'Upper':
            result = raw_activation_key[:start_index] + raw_activation_key[start_index:end_index].upper() + raw_activation_key[end_index:]
            print(result)
        elif letter == 'Lower':
            result = raw_activation_key[:start_index] + raw_activation_key[start_index:end_index].lower() + raw_activation_key[end_index:]
            print(result)
    elif operation == 'Slice':
        operation, start_index, end_index = command[0], command[1], command[2]
        result = raw_activation_key[:start_index] + raw_activation_key[end_index:]











