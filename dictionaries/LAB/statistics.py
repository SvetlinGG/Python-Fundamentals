
products = input().split(': ')
materials = {}
while products != 'statistics':
    products = input().split(': ')

    key = products[0]
    value = products[1]
    materials[key] = int(value)
    if key == 'statistics':
        break
print(len(materials.keys()))