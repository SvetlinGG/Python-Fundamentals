initial_list = [ str(word) for word in input().split('!')]

for _ in initial_list:

    command = input().split(' ')
    if command[0] == 'Urgent':
        if command[1]:
            continue
        initial_list[0] += command[1]
    elif command[0] == 'Unnecessary':
        if command[1]:
            continue
        initial_list.remove(command[1])
    elif command[0] == 'Correct':
        if command[1]:
            continue
        initial_list.remove(command[1])
        initial_list[1] += command[1]
    elif command[0] == 'Rearrange':
        if command[1]:
            continue
        initial_list.remove(command[1])
        initial_list.append(command[1])
    elif command[0] == 'Go':
        break

print(', '.join(initial_list))


