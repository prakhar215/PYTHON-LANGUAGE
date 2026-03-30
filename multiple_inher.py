class Teacher:
    def __init__(self,salary):
        self.salary=salary
class Student:
    def __init__(self,cgpa):
        self.cgpa=cgpa
class TA(Teacher,Student):
    def __init__(self,salary,cgpa,Name):
        super().__init__(salary)
        Student.__init__(self,cgpa)
        self.name=Name
ta21=TA(1000,8.3,"Akash")
print(ta21.name,ta21.cgpa,ta21.salary)