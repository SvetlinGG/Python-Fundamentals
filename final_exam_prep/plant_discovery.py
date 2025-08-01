
num = int(input())

plant = {}
for _ in range(num):
    plant_name, rarity = input().split('<->')
    rarity = int(rarity)
    plant[plant_name] = {"rarity": 0, "rating": 0}


    command = input()
    while command[0] != 'Exhibition':
        operation = command.split(': ')
        operation_type = operation[0]
        command = input()
        print(operation[0])

#plant_info = {}
# rarity_d, rating_d = "Rarity", "Rating"
# for plant in range(number_of_pants):
#     plant_name, plant_rarity = input().split("<->")
#     plant_info[plant_name] = plant_info.get(plant_name, {})
#     plant_info[plant_name][rarity_d] = float(plant_rarity)
#     plant_info[plant_name][rating_d] = []