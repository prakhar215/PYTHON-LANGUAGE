class Employee:
    def get_designation(self):
        print("deignation is Employee")
class Teacher:
    def get_designation(self):
        print("Designation is teacher")
t1=Teacher()
t1.get_designation()
t2=Employee()
t2.get_designation()