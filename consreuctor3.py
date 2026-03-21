class mobile:
    def __init__(self,model,price):
        self.Model=model
        self.Price=price
    def get_Model(self):
        return self.Model
    def get_Price(self):
        return self.Price 
nokia=mobile(1133,10000)
apple=mobile(17,82000)
print(f"The model name is {nokia.get_Model()} and price is {nokia.get_Price()} ")