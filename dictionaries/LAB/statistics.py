

materials = {}
while True:
    command = input()
    if command == 'statistics':
        break

    product, quantity = command.split(': ')

    key = product
    value = int(quantity)
    materials[key] = value

    count_all_products = len(materials.keys())
    sum_all_quantities = sum(materials.values())
print(count_all_products)
print(sum_all_quantities)
print(materials)