

password = input()

command = input().split(' ')
while command[0] != 'Done':

        operation = command[0]
        if operation == 'TakeOdd':
            password = password[1::2]
            print(password)
        elif operation == 'Cut':
            cur_index, length = int(command[1]), int(command[2])
            substring = password[cur_index:cur_index+length]
            password = password.replace(substring, "", 1)
            print(password)
        elif operation == 'Substitute':
            substring, substitute = command[1], command[2]
            if substring in password:
                password = password.replace(substring, substitute)
                print(password)
            else:
                print('Nothing to replace!')
        command = input().split(' ')

print(f'Your password is: {password}')


