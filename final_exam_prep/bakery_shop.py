
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
        if food_type is not food['food_type']:
            food['food_type'] = food['food_type']
            if food[quantity] <= 0:
                continue
    elif operation == 'Sell':
        quantity = int(command[1])
        food_type = command[2]
        if food_type is not food['food_type']:
            print(f'You do not have any {food_type}.')



