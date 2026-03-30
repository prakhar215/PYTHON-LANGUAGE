class phone:
    company="apple"
    price_range="50k-200k"
class Specification(phone):
    def __init__(self,processor):
        self.processor=processor
app17=Specification("A17")
print(app17.processor,app17.company,app17.price_range)