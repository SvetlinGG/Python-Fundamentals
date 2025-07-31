
message = input()

command = input()
while command[0] != 'Reveal':

    operation = command.split(':|:')
    command_type = operation[0]
    if command_type == 'InsertSpace':
        cur_index = int(operation[1])
        message = message[:cur_index] + ' ' + message[cur_index:]
        print(message)
    elif command_type == 'Reverse':
        substring = operation[1]
        if substring in message:
            message = message.replace(substring, '', 1)
            message += substring[::-1]
            print(message)
        else:
            print('error')
    elif command_type == 'ChangeAll':
        substring, replacement = operation[1], operation[2]
        message = message.replace(substring, replacement)
        print(message)
    command = input()

print(f'You have a new text message: {message}!')
