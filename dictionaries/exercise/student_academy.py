
pair_of_rows = int(input())

academy = {}

for _ in range(pair_of_rows):

    student = input()
    grade = float(input())

    if student not in academy:
        academy[student] = []
    academy[student].append(grade)

for students, grades in academy.items():
    avg = sum(grades) / len(grades)
    if avg < 4.5:
        continue
    print(f'{students} -> {avg:.2f}')