
cities = {}
command = input().split('||')
while command[0] != 'Sail':

    city, population, gold = command[0], int(command[1]), int(command[2])

    if city not in cities.keys():
        cities[city] = {"population": population, "gold": gold}
        command = input().split('||')


cities = {"Tortuga":
              {"population": population,
               "gold": gold}}