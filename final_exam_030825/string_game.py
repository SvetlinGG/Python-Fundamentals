
main_string = input()

command = input().split(' ')
while command[0] != 'Done':

    operation = command[0]
    if operation == 'Change':
        char, replacement = command[1], command[2]
        main_string = main_string.replace(char, replacement)
        print(main_string)
    elif operation == 'Includes':
        substring = command[1]
        if substring in main_string:
            print(True)
        else:
            print(False)
    elif operation == 'End':
        substring = command[1]
        if substring in main_string[-len(substring)]:
            print(True)
        else:
            print(False)
    elif operation == 'Uppercase':
        main_string = main_string.upper()
        print(main_string)
    elif operation == 'FindIndex':
        char = command[1]
        print(main_string.find(char))
    elif operation == 'Cut':
        start_index = int(command[1])
        count = int(command[2])
        cut_part = main_string[start_index:start_index + count]
        print(cut_part)



    command = input().split(' ')

