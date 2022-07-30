from abc import ABC, abstractmethod
from typing import List


class AnimalTest:
    @staticmethod
    def main(*args):
        at: AnimalTest = AnimalTest()
        at.makeSomeAnimals()
    
    def makeSomeAnimals(self):
        dog: Animal = self.Dog()
        cat: Animal = self.Cat()
        # treat dogs and cats as their supertype, Animal
        animals: List[Animal] = []
        animals.append(dog)
        animals.append(cat)
        for animal in animals: animal.makeSound() # can call makeSound on any Animal
            
    class Animal(ABC):
        @abstractmethod
        def makeSound(self) -> None:
            raise NotImplementedError
    
    class Dog(Animal):
        def makeSound(self) -> None:
            self.bark()
            
        def bark(self) -> None:
            print('Woof')
            
    class Cat(Animal):
        def makeSound(self) -> None:
            self.meow()
            
        def meow(self) -> None:
            print('Meow')

        
if __name__ == "__main__":
    AnimalTest.main()