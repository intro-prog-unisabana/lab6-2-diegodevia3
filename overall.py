def student_averages(students):
    result = {}
    for student, grades in students.items():
        avg = sum(grades.values()) / len(grades)
        result[student] = round(avg)
    return result


def assignment_averages(students):
    assignment_totals = {}
    assignment_counts = {}

    for grades in students.values():
        for assignment, score in grades.items():
            assignment_totals[assignment] = assignment_totals.get(assignment, 0) + score
            assignment_counts[assignment] = assignment_counts.get(assignment, 0) + 1

    result = {}
    for assignment in assignment_totals:
        avg = assignment_totals[assignment] / assignment_counts[assignment]
        result[assignment] = round(avg)

    return result