products = input()
quantity = int(input())

def orders(products, quantity):

    if products == 'coffee':
        price = 1.50
    elif products == 'water':
        price = 1.00
    elif products == 'coke':
        price = 1.40
    elif products == 'snacks':
        price = 2.00

    result = price * quantity

    return print(f'{result:.2f}')

orders(products, quantity)