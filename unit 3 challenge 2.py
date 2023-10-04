class Student:
  def __init__(self, name, rollnumber, cgpa):
    self.name = name
    self.rollnumber = rollnumber
    self.cgpa = cgpa
def sortstudents(studentlist):
  sortedstudents = sorted(studentlist,                          key=lambda student: student.cgpa,                         reverse=True)
  return sortedstudents
students = [
    Student("kavitha", "37", 1.1),
    Student("karthi", "73", 2.2),
    Student("kaviya", "78", 3.3),
    Student("nisha", "80", 4.4),
]
sortedstudents = sortstudents(students)
for student in sortedstudents:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,      student.rollnumber, student.cgpa));