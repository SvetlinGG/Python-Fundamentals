
cities = {}
command = input().split('||')
while command[0] != 'Sail':

    city, population, gold = command[0], int(command[1]), int(command[2])

    if city not in cities.keys():
        cities[city] = {"population": population, "gold": gold}
    cities[city]["population"] += population
    cities[city]["gold"] += gold
    command = input().split('||')

command = input().split('=>')
while command[0] != 'End':

    if command[0] == 'Plunder':
        town, people, gold = command[1], int(command[2]), int(command[3])
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
        cities[town]['population'] -= people
        cities[town]['gold'] -= gold
        if cities[town]['population'] == 0 or cities[town]['gold'] == 0:
            del cities[town]
            print(f'{town} has been wiped off the map!')
    elif command[0] == 'Prosper':
        town, gold = command[1], int(command[2])
        if gold < 0:
            print(f'Gold added cannot be a negative number!')
        else:
            cities[town]['gold'] += gold
            total_gold = cities[town]['gold']
            print(f'{gold} gold added to the city treasury. {town} now has {total_gold} gold.')

    command = input().split('=>')





