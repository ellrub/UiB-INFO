from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def skinType(self, type):
        if type == 'mammal':
            return 'hair'
        elif type == 'reptile':
            return 'scales'
        elif type == 'bird':
            return 'feathers'

class Mammal(Animal):
    pass

class Reptile(Animal):
    pass

class Birds(Animal):
    pass

class Dog(Mammal):
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print('Dog barks!')

dog = Dog('Fido', 'Dog')
dog.speak()
