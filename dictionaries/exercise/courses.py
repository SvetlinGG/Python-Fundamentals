
courses = {}


while True:
    course = input()

    if course == 'end':
        break
    course_name, student_name = course.split(' : ')

    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)
for course_name, student_name in courses.items():
    print(f'{course_name}: {len(student_name)}')
    for student in student_name:
        print(f'-- {student}')

