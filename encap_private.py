class account:
    def __init__(self,name,balance):
        self.Name=name
        self.__balance=balance
    def get_bal(self):
        return self.__balance
acc1=account("prakhar",10000)
acc2=account("anuj",9000)
print(acc1.Name)
print(acc2.get_bal())