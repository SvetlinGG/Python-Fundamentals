
orders = {}

while True:

    order = input()
    if order == 'buy':
        break
    product, price, quantity = order.split()
    price = float(price)
    quantity = int(quantity)
    if product not in orders:
        orders[product] = [price, quantity]
    else:
        orders[product][1] += quantity
        if orders[product][0] != price:
            orders[product][0] = price

for products, (prices, quantity) in orders.items():
    print(f'{products} -> {prices * quantity:.2f}')

orders = {}

# while True:
#     command = input()
#     if command == 'buy':
#         break
#
#     product, price, quantity = command.split()
#     price = float(price)
#     quantity = int(quantity)
#
#     if product not in orders:
#         orders[product] = [price, quantity]
#     else:
#         orders[product][1] += quantity
#         if orders[product][0] != price:
#             orders[product][0] = price
#
# for product, (price, quantity) in orders.items():
#     print(f'{product} -> {price * quantity:.2f}')
