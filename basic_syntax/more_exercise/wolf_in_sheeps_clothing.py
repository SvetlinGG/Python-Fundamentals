animals = input().split(', ')
for i in range(len(animals) - 1):
    
    next_one = animals[i + 1]
    if next_one == 'wolf':
        print('Please go away and stop eating my sheep')
    else:
        print(f'Oi! Sheep number {i + 1}! You are about to be eaten by a wolf!')