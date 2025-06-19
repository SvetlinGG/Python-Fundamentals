
employee_efficiency = [ int(input()) for _ in range(4)]
student_count = employee_efficiency[-1]
student_per_hour = 0
time = 0

for student in employee_efficiency:
    student_per_hour += student
    if student_count > student_per_hour:
        if student_count / student_per_hour > 1:
            time += 1
            print(f'Time needed: {time}h.')



