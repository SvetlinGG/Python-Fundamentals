orders = int(input())


total_price = 0

for _ in range(orders):

    price_per_capsules = float(input())
    days = int(input())
    caps_per_day = int(input())
    if 0.01 <= price_per_capsules <= 100 and 1 <= days <= 31 and 1 <= price_per_capsules <= 2000:
        price = price_per_capsules * days * caps_per_day
        total_price += price
        print(f'The price for the coffee is: ${price:.2f}')

print(f'Total: ${total_price:.2f}')