from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Lion(Animal):
    def make_sound(self):
        print("ROAR!")
class Dog(Animal):
    def make_sound(self):
        print("BARK!")
class Cow(Animal):
    def make_sound(self):
        print("MOO!")
lion=Lion()
lion.make_sound()
cow=Cow()
cow.make_sound()
dog=Dog()
dog.make_sound()