command = input()
events = ["coding", "dog", "cat", "movie"]
coffee_count = 0

while command != 'END':
    if command.lower() in events:
        if command in events:
            coffee_count +=1
        else:
            coffee_count +=2
    command = input()
if coffee_count > 5:
    print('You need extra sleep')
else:
    print(coffee_count)