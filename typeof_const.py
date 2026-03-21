class student:
    def __init__(self):
        print("Constructor is called")
class student1:
    def __init__(self,name,cgpa):
        self.Name=name
        self.Cgpa=cgpa
    def get_Name(self):
            return self.Name
    def get_Cgpa(self):
         return self.Cgpa
stu1=student()
stu2=student()
stu3=student1("prak",20)
stu4=student1("anuj",21)
print(stu3.get_Name())
print(stu4.get_Cgpa())