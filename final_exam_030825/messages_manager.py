
capacity = int(input())

username = {}

command = input()
while command != 'Statistics':

    username = {"name": 'name', "sent": 0, "received": 0}
    command = input().split('=')
    operation = command[0]
    if operation == 'Add':
        name = command[1]
        sent = int(command[2])
        received = int(command[3])
        if name in username:
            continue
        else:
            username["name"] = name
            username["sent"] += sent
            username["received"] += received
    elif operation == 'Message':
        sender = command[1]
        receiver = command[2]
        if sender in username and receiver in username:
            username[sender][sent] += 1
            username[receiver][received] += 1
        capacity_sender = username[sender]["sent"] + username[sender]["received"]
        capacity_receiver = username[receiver]["sent"] + username[receiver]["received"]
        if capacity_sender > capacity or capacity_receiver > capacity:
            del username[sender]
            del username[receiver]
            print(f'{username} reached the capacity!')
    elif operation == 'Empty':
        del username[command[1]]


    command = input()
for user, num_messages in username.items():
    print(f"{user}: {num_messages}")