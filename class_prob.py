class Product:
    count=0
    def __init__(self,name,price):
        self.Name=name
        self.price=price
        Product.count+=1
    def get_info(self):
        print(f"The price of {self.Name} is {self.price}")
    @classmethod
    def get_count(cls):
        print(f"The total number of product is {cls.count}")
    @staticmethod
    def cal_dicount(price,discount):
        print(f"The discounted price is {price -(price*discount)/100}")
phone1=Product("apple",70000)
phone2=Product("samsung",52000)
product3=Product("oppo",21000)
phone1.get_info()
Product.get_count()
Product.cal_dicount(82000,5)