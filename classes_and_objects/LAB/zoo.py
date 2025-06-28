
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

    def get_info(self, species):
        pass
zoo_name = input()
zoo = Zoo(zoo_name)
total_animals = 0
for i in range(number):
