number_of_students = int(input())
students_and_grades = {}
average_grade = []
for i in range(number_of_students):

    student, grade = input().split(" ")
    grade = float(grade)

    if student not in students_and_grades.keys():
        students_and_grades[student] = []

    students_and_grades[student].append(grade)

for key, value in students_and_grades.items():
    average_grade = sum(value)
    average_grade = average_grade / len(value)

    print(f"{key} ->", end=" ")
    for i in value:
        print(f'{i:.2f}', end=" ")
    print(f"(avg: {average_grade:.2f})")
