

# keys = ['name', 'age', 'major']
# values = ['Ivan', 22, 'Developer']
#
# student = {}
#
# for i in range(len(keys)):
#     key = keys[i]
#     value = values[i]
#
#     student[key] = value
# print(student)
# print(student.keys())
# print(student.values())
# print(student.items())

student = {
    'name': 'Ivan',
    'age': 22,
    'major': 'Developer',
    'language': 'Python',
}
student['grade'] = 'Excellent'
print(student)
# print(student.get('name'))
# print(student.get('language'))
print(student.items())
print(student.keys())
print(student.values())