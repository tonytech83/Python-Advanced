n = int(input())

# dict where to store uniq students names
students_grades = {}

for _ in range(n):
    # unpack the input from console
    name, grade = input().split()

    # if the name does not exist in dict add it, else append grade to this name
    if name not in students_grades.keys():
        students_grades[name] = []
    students_grades[name].append(float(grade))

# on each loop unpack the name and its grades.
for student_name, grades in students_grades.items():
    grades_formatted = [f'{x:.2f}' for x in grades]
    avg_grade = sum(grades) / len(grades)
    print(f'{student_name} -> {" ".join(grades_formatted)} (avg: {avg_grade:.2f})')
