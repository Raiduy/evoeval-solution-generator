
def class_grades_with_flip(name_grade_list):
    gpa_to_letter_grade = {4.0: 'A+', 3.7: 'A', 3.3: 'A-', 3.0: 'B+', 2.7: 'B', 2.3: 'B-', 2.0: 'C+', 1.7: 'C', 1.3: 'C-', 1.0: 'D+', 0.7: 'D', 0.0: 'D-', 0.0: 'E'}
    results = []
    for (name, gpa) in name_grade_list:
        name = name.title()
        letter_grade = gpa_to_letter_grade.get(gpa, 'E')
        results.append((name, letter_grade))
    return results