stock = input().split(' ')

products = {}

for i in range(0, len(stock), 2):
    key = stock[i]
    value = stock[i + 1]
    products[key] = int(value)

search = input().split()
for item in search:
    if item in products:
        print(f'We have {products[item]} of {item} left')
    else:
        print(f"Sorry, we don't have {item}")