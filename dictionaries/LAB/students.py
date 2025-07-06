
students_info = input()
students = {}

while not students.get(students_info):

    course = input().split(':')
    name = course[0]
    id_ = course[1]
    course_name = course[2]
    print(f'- {course_name}: {course}')

    if course_name == students_info:
        students[name, id_]  = course_name

for (key, value) in students.items():
    print(f'- {key} - {value}')