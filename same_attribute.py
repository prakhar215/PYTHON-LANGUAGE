class Student:
    college_name="global"
    cgpa=7.2
    def __init__(self,name):
        self.name=name
        self.cgpa=7.2
student1=Student("prak")
print(student1.cgpa)
print(Student.cgpa)