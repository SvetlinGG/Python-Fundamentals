wagons  = int(input())
train = [0] * wagons

while True:

    command = input().split()


    if command == 'End':
        break
    if command[0] == 'add':
        train[-1] += int(command[1])
    elif command[0] == 'insert':
        index = int(command[1])
        train[index] = int(command[2])
    elif command[0] == 'leave':
        index = int(command[1])
        train[index] -= int(command[2])
        print(train)







# train_wagons = int(input())
# train = [0] * train_wagons
# command = input()
#
#
# def add_people(people):
#     train[-1] += people
#
# def insert_people(wagon, number_people):
#     train[wagon] += number_people
#
# def leave_people(wagon, number_people):
#     train[wagon] -= number_people
#
#
# commands = {
#     "add": add_people,
#     "insert": insert_people,
#     "leave": leave_people
# }
#
# while command != "End":
#     command, *info = [int(x) if x.isdigit() else x for x in command.split()]
#     commands[command](*info)
#     command = input()
#
# print(train)

# train_wagons = int(input())
# train = [0] * train_wagons
# for _ in range(train_wagons):
#     command = input().split(' ')
#     if command[0] == 'add':
#         train[-1] += int(command[1])
#     elif command[0] == 'insert':
#         train[int(command[1])] = int(command[2])
#     elif command[0] == 'leave':
#         train[int(command[1])] -= int(command[2])
#     elif command[0] == 'End':
#         break
# print(train)


