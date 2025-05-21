animals = input().split(', ')
animals.reverse()

if animals[0] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    print(f'Oi! Sheep number {animals.index("wolf")}! You are about to be eaten by a wolf!')