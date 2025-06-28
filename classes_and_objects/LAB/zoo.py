
class Zoo:
    _animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
         if species == 'mammal':
             self.mammals.append(name)
        elif species == 'fish':
             self.fishes.append(name)
        elif species == 'bird':
             self.birds.append(name)

        Zoo._animals += 1

    def get_info(self, species):
        result = ""
        if species == 'mammal':
            result += f"Mammals in {self.name}: {", ".join(self.mammals)}\n"
        elif species == 'fish':
            result += f"Fishes in {self.name}: {", ".join(self.fishes)}\n"
        elif species == 'bird':
            result += f"Birds in {self.name}: {", ".join(self.birds)}\n"

        result += f'Total animals: {Zoo._animals}'
        return result
zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input)
for i in range(count):
