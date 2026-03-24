class account:
    def __init__(self,name,balance):
        self.Name=name
        self.__balance=balance
    def get_bal(self):     #getter function
        return self.__balance
acc1=account("prakhar",10000)
acc2=account("anuj",9000)
print(acc1.Name,acc1.get_bal(),acc2.get_bal())