
number_of_cars = int(input())

while (command := input()) != 'Stop':

    car, mileage, fuel = command.split('|')

    print(car)
    print(mileage)
    print(fuel)

    command = input()
    operation, car, distance, fuel = command.split(':')
    print(operation)
    print(car)
    print(distance)
    print(fuel)
