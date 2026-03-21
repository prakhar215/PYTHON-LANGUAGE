class student:
    def __init__(self,name,age,cgpa):
        self.Name =name
        self.Age = age
        self.cgpa=cgpa
student1=student("prakhar",20,7.0)
student2=student("anuj",20,7.1)
student3=student("abhiraj",20,7.2)
print(student1.Name)
print(student2.Age)
print(student3.cgpa)