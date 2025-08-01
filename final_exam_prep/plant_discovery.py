
n = int(input())
plants = {}

for _ in range(n):
    plant_data = input()
    plant, rarity = plant_data.split("<->")
    rarity = int(rarity)
    if plant not in plants:
        plants[plant] = {"rarity": rarity, "ratings": []}
    else:
        plants[plant]["rarity"] = rarity


while True:
    command_line = input()
    if command_line == "Exhibition":
        break

    try:
        command, rest = command_line.split(": ")
        if command == "Rate":
            plant, rating = rest.split(" - ")
            rating = float(rating)
            if plant in plants:
                plants[plant]["ratings"].append(rating)
            else:
                print("error")
        elif command == "Update":
            plant, new_rarity = rest.split(" - ")
            new_rarity = int(new_rarity)
            if plant in plants:
                plants[plant]["rarity"] = new_rarity
            else:
                print("error")
        elif command == "Reset":
            plant = rest
            if plant in plants:
                plants[plant]["ratings"] = []
            else:
                print("error")
        else:
            print("error")
    except ValueError:
        print("error")

print("Plants for the exhibition:")
for plant, data in plants.items():
    ratings = data["ratings"]
    avg_rating = sum(ratings) / len(ratings) if ratings else 0
    print(f"- {plant}; Rarity: {data['rarity']}; Rating: {avg_rating:.2f}")







