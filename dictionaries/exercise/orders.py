
orders = {}

while True:

    order = input()
    if order == 'buy':
        break
    product, price, quantity = order.split()
    total_sum = float(price) * int(quantity)
    orders[product] = total_sum
for products, prices in orders.items():
    print(f'{products} -> {prices:.2f}')