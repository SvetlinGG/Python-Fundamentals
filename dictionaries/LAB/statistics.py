

materials = {}

while True:

    command = input()
    if command == 'statistics':
        break

    product, quantity = command.split(': ')

    key = product
    value = int(quantity)

    if product not in materials:
        materials[product] = 0
    materials[product] += value
print('Products in stock:')

for (key, value) in materials.items():
    print(f'- {key}: {value}')

print(f'Total Products: {len(materials.keys())}')
print(f'Total Quantity: {sum(materials.values())}')



