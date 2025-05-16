orders = int(input())


total_price = 0

for _ in range(orders):

    price_per_capsules = float(input())
    days = int(input())
    caps_per_day = int(input())
    if  price_per_capsules >= 0.01 or price_per_capsules <= 100 and days >= 1 or days <= 31 and caps_per_day >= 1 or caps_per_day <= 2000:
        price = price_per_capsules * days * caps_per_day
        if price <= 0:
            continue
        total_price += price
        print(f'The price for the coffee is: ${price:.2f}')

print(f'Total: ${total_price:.2f}')