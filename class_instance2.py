class Laptop:
    storage_type="SSD"
    def __init__(self,RAM,storage):
        self.RAM=RAM
        self.storage=storage
    def get_info(self):
        print(f"The Laptop has {self.storage_type} and RAM {self.RAM} and storage is {self.storage}")
lap1=Laptop("12GB","512GB")
lap2=Laptop("16GB","1024GB")
lap1.get_info()