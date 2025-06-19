
employee_efficiency = [ int(input()) for _ in range(4)]
student_per_hour = sum(employee_efficiency[:-1])
student_count = employee_efficiency[-1]

time = 0

while student_count > 0:
    time += 1

    if time % 4 != 0:
        student_count -= student_per_hour

print(f'Time needed: {time}h.')

