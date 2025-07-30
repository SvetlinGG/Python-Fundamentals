raw_activation_key = input()

while True:
    command = input()
    if command == 'Generate':
        break

    parts = command.split('>>>')
    operation = parts[0]

    if operation == 'Contains':
        substring = parts[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif operation == 'Flip':
        case_type = parts[1]
        start_index = int(parts[2])
        end_index = int(parts[3])

        if case_type == 'Upper':
            raw_activation_key = (
                raw_activation_key[:start_index] +
                raw_activation_key[start_index:end_index].upper() +
                raw_activation_key[end_index:]
            )
        elif case_type == 'Lower':
            raw_activation_key = (
                raw_activation_key[:start_index] +
                raw_activation_key[start_index:end_index].lower() +
                raw_activation_key[end_index:]
            )
        print(raw_activation_key)

    elif operation == 'Slice':
        start_index = int(parts[1])
        end_index = int(parts[2])
        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
        print(raw_activation_key)

print(f"Your activation key is: {raw_activation_key}")




# raw_activation_key = input()
#
# command = input().split('>>>')
#
# while command[0] != 'Generate':
#     command = input().split('>>>')
#     operation = command[0]
#     if operation == 'Contains':
#         substring = command[1]
#         if substring in raw_activation_key:
#             print(f'{raw_activation_key} contains {substring}.')
#         else:
#             print(f'Substring not found!')
#     elif operation == 'Flip':
#         letter, start_index, end_index = command[1], int(command[2]), int(command[3])
#         if letter == 'Upper':
#             raw_activation_key = (raw_activation_key[:start_index] + raw_activation_key[start_index:end_index].upper() + raw_activation_key[end_index:])
#             print(raw_activation_key)
#         elif letter == 'Lower':
#             raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[start_index:end_index].lower() + raw_activation_key[end_index:]
#             print(raw_activation_key)
#     elif operation == 'Slice':
#         start_index, end_index = int(command[1]), int(command[2])
#         raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
#         print(raw_activation_key)
#     command = input().split('>>>')
# print(f'Your activation key is: {raw_activation_key}"')











