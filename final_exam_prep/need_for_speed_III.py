
number_of_cars = int(input())

while (command := input()) != 'Stop':

    cars = command.split('|')
    model = cars[0]
    mileage = cars[1]
    fuel = cars[2]
    print(model)
    print(mileage)
    print(fuel)
