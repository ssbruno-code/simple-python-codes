student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {
    "Harry": " ",
    "Ron": " ",
    "Hermione": " ",
    "Draco": " ",
    "Neville": " ",  
}


for student in student_scores:
    if student_scores[student] > 90:
        student_grades[student] = "Outstandig"
        print(student)
        print(student_grades[student])
    elif student_scores[student] > 80:
        student_grades[student] = "Exceeds Expectations"
        print(student)
        print(student_grades[student])
    elif student_scores[student] > 70:
        student_grades[student] = "Acceptable"
        print(student)
        print(student_grades[student])
    else:
        student_grades[student] = "Fail"
        print(student)
        print(student_grades[student])