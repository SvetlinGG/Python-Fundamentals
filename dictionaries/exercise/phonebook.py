
phonebook = {}

while True:

    people = input()

    if '-' not in people:
        break

    name, number = people.split('-')
    phonebook[name] = number
searched = int(people)

for search in range(searched):
    search_name = input()
    if search_name in phonebook.keys():
        print(f'{search_name} -> {phonebook[search_name]}')
    else:
        print(f'Contact {search_name} does not exist.')

