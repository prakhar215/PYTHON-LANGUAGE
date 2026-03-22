class Laptop:
    storage_type="SSD"
    def __init__(self,RAM,storage):
        self.RAM=RAM
        self.storage=storage
    @classmethod
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type} ")
    def get_info(self):
        print(f"The Laptop has {self.storage_type} and RAM {self.RAM} and storage is {self.storage}")
    @staticmethod
    def disc_price(price,discount):
        final_price=price -(discount*price)/100
        print(f"The DIscounted price is {final_price}")
lap1=Laptop("12GB","512GB")
lap2=Laptop("16GB","1024GB")
lap1.disc_price(50000,10)