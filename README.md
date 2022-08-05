# Python Head First Design Patterns  
## Chapters  
[chapter 1](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/strategy)-done  
[chapter 2](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/observer)-done (Only swing has no translation.)  
[chapter 3](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/decorator)-done (Only io has no translation.)  
[chapter 4](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/factory)-done  
[chapter 5](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/singleton)-done  
[chapter 6](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/command)-done (Only swing has no translation.)  
[chapter 7(adapter)](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/adapter)-done  
[chapter 7(facade)](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/facade/hometheater)-done  
  
## Introduction  
1. Translated from [Head-First-Design-Patterns](https://github.com/bethrobson/Head-First-Design-Patterns) (java)  
2. What are the differences between other Python version Head-First-Design-Patterns and ours?  
     - We named the files with the same name and path as the original. (The following examples are from Chapter 1.)  
          ![image](https://user-images.githubusercontent.com/57841111/182039744-241d304f-9159-4019-bf11-8e798d4041ce.png)  
     - We annotate the type of the code so that the code we translate is closer to the java version. (The following examples is from strategy/AnimalTest.py.)   
         ```python3
            # our code
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
         ```
         ```java
            // authors' code [https://github.com/bethrobson/Head-First-Design-Patterns/blob/master/src/headfirst/designpatterns/strategy/AnimalTest.java]
            import java.util.ArrayList;

            public class AnimalTest {

              public static void main(String[] args) {
                AnimalTest at = new AnimalTest();
                at.makeSomeAnimals();
              }
              public void makeSomeAnimals() {
                Animal dog = new Dog();
                Animal cat = new Cat();
                // treat dogs and cats as their supertype, Animal
                ArrayList<Animal> animals = new ArrayList<Animal>();
                animals.add(dog);
                animals.add(cat);
                animals.forEach(Animal::makeSound); // can call makeSound on any Animal
              }
         ```


