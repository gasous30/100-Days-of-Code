student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}
for name in student_scores:
    grades = student_scores[name]
    if(grades <= 100 and grades > 90):
        grades_expressed = "Outstanding"
    elif(grades <= 90 and grades > 80):
        grades_expressed = "Exceeds Expectations"
    elif(grades <= 80 and grades > 70):
        grades_expressed = "Acceptable"
    else:
        grades_expressed = "Fail"
        
    student_grades[name] = grades_expressed

print(student_grades)