from collections import defaultdict


students = defaultdict(list)
number_of_inputs = int(input())

for _ in range(number_of_inputs):
    name, grade = input().split()
    students[name].append(float(grade))

for name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    format_grades = list(map(lambda x: f"{x :.2f}", grades))
    print(f"{name} -> {' '.join(format_grades)} (avg: {average_grade :.2f})")

