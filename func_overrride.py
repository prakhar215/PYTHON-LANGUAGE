class Employee:
    def get_designation(self):
        print("deignation = Employee")
class Teacher(Employee):
    def get_designation(self):
        print("DEsignation is teacher")
t1=Teacher()
t1.get_designation()