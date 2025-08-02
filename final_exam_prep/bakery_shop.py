
food = {}
while True:
    command = input().split(' ')
    operation = command[0]

    if operation == 'Complete':
        break

    quantity = int(command[1])
    food_type = command[2]
    food = {"food_type": food_type, "quantity": quantity}
    if operation == 'Receive':
        food.update()
        print(food)
    #command = input().split(' ')

