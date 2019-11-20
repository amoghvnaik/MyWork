from abc import ABC, abstractmethod

class animal(ABC):
    def __init__(self,type):
        self.type = type
    @abstractmethod
    def speak(self):
        pass

class dog(animal):
    def __init__(self,name):
        super().__init__('mammal')
        self.name = name
    def speak(self):
        print('bark')

pet = dog('pep')
print(pet.name)
print(pet.type)
dog('pep').speak()
