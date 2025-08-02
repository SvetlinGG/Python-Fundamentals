







# food = {}
# while True:
#     command = input().split(' ')
#     operation = command[0]
#
#     if operation == 'Complete':
#         break
#
#     quantity = int(command[1])
#     food_type = command[2]
#
#     if operation == 'Receive':
#         if quantity <= 0:
#             continue
#         if food_type not in food:
#             food[food_type] = 0
#         food[food_type] += quantity
#
#     elif operation == 'Sell':
#         if food_type not in food:
#             print(f'You do not have any {food_type}.')
#         elif food[food_type] < quantity:
#             print(f"There aren't enough {food_type}. You sold the last {food[food_type]}.")
#             del food[food_type]
#         else:
#             food[food_type] -= quantity
#             print(f'You sold {quantity} {food_type}.')
#             if food[food_type] == 0:
#                 del food[food_type]
#
#
# for item, qty in food.items():
#     print(f'{item}: {qty}')







    # food = {"food_type": food_type, "quantity": quantity}
    # if operation == 'Receive':
    #     food.update()
    #     if food_type != food['food_type']:
    #         food['food_type'] = food['food_type']
    #         if food[quantity] <= 0:
    #             continue
    # elif operation == 'Sell':
    #     quantity = int(command[1])
    #     food_type = command[2]
    #     if food_type != food['food_type']:
    #         print(f'You do not have any {food_type}.')



