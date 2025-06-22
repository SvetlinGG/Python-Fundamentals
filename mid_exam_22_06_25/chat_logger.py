chat_log = []

while True:
    command_line = input()
    if command_line == "end":
        break

    parts = command_line.split()
    command = parts[0]

    if command == "Chat":
        message = parts[1]
        chat_log.append(message)

    elif command == "Delete":
        message = parts[1]
        if message in chat_log:
            chat_log.remove(message)

    elif command == "Edit":
        old_message = parts[1]
        new_message = parts[2]
        if old_message in chat_log:
            index = chat_log.index(old_message)
            chat_log[index] = new_message

    elif command == "Pin":
        message = parts[1]
        if message in chat_log:
            chat_log.remove(message)
            chat_log.append(message)

    elif command == "Spam":
        messages = parts[1:]
        chat_log.extend(messages)


for message in chat_log:
    print(message)


# from os.path import exists
#
# message = input().split()
#
# while True:
#
#     operation = input()
#
#     command = operation.split(' ')
#     action = command[0]
#     name = command[1]
#     name_2 = command[2]
#
#     if action == 'Chat':
#         message.append(command[1])
#     elif action == 'Delete':
#         if exists(command[1]):
#             message.remove(command[1])
#     elif action == 'Edit':
#         index = message.index(name)
#         message[index] = name_2
#         if not exists(command[1]):
#             continue
#     elif action == 'Pin':
#         message.append(command[1])
#         if not exists(command[1]):
#             continue
#     elif action == 'Spam':
#         message.append(command[1])
#     elif action == 'end':
#         break
# print(message)

