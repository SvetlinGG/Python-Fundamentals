

keys = ['name', 'age', 'major']
values = ['Ivan', 22, 'Developer']

student = {}

for i in range(len(keys)):
    key = keys[i]
    value = values[i]

    student[key] = value
print(student)