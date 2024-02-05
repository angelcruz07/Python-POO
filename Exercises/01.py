class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def study(self):
        print(f'The student {self.name} is studying')

name = input("Enter the student's name: ")
age = input("What is the student's age: ")
grade = input("In which grade is the student: ")

student = Student(name, age, grade)

print(f"""
  STUDENT INFORMATION:
    Name: {student.name}
    Age: {student.age}
    Grade: {student.grade}
""")

while True:
    study_input = input()
    if study_input.lower() == "study":
        student.study()
        break