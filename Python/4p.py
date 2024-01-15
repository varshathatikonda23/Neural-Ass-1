student_score = float(input("Write the class score: "))

if 90 <= student_score <= 100:
   student_grade = 'A'
elif 80 <= student_score < 90:
    student_grade = 'B'
elif 70 <= student_score < 80:
    student_grade = 'C'
elif 60 <= student_score < 70:
    student_grade = 'D'
elif 0 <= student_score < 60:
    student_grade = 'F'
else:
    student_grade = 'The score is invalid'

print(f"The grade for the score {student_score} is: {student_grade}")