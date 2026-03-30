class Employee:
    start_time="10PM"
    end_time="6PM"
class Adminstaff(Employee):
    def __init__(self,role):
        self.role=role
class Accountant(Adminstaff):
    def __init__(self,salary,role):
        super().__init__(role)
        self.salary=salary
acc1=Accountant(29000,"CA")
print(acc1.role,acc1.start_time,acc1.end_time)