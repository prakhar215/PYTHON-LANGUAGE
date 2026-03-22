class student:
    college_name="global"
    def __init__(self,name,cgpa):
        self.Name=name
        self.Cgpa=cgpa
stu1=student("anuj",7.2)
print(stu1.Name)
print(stu1.Cgpa)
print(student.college_name)