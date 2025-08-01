

password = input()

command = input().split(' ')
while command[0] != 'Done':

     operation = command
        if operation == 'TakeOdd':
            print(password[1::2])
        elif operation == 'Cut':
            cur_index, length = int(command[1]), int(command[2])
            


