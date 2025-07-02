materials = input().split(' ')

bakery = {}

for i in range(0, len(materials), 2):
    key = materials[i]
    value = materials[i + 1]
    bakery[key] = int(value)
print(bakery)

