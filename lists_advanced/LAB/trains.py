train_wagons = int(input())
train = [0] * train_wagons
for _ in range(train_wagons):
    command = input().split(' ')
    if command[0] == 'add':
        train[-1] += int(command[1])
    if command[0] == 'insert':
        train.insert(train[0], int(command[2]))
print(train)


