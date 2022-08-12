# Python Head First Design Patterns  
## Don't forget to give this repository a star, thanks.  
## Chapters  
[chapter 1(strategy)](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/strategy)  
[chapter 2(observer)](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/observer) (Only swing has no translation.)  
[chapter 3(decorator)](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/decorator) (Only io has no translation.)  
[chapter 4(factory)](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/factory)  
[chapter 5(singleton)](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/singleton)  
[chapter 6(command)](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/command) (Only swing has no translation.)  
[chapter 7(adapter)](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/adapter)  
[chapter 7(facade)](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/facade/hometheater)  
[chapter 8(templatemethod)](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/templatemethod) (applet and frame have no translation.)  
[chapter 9(iterator)](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/iterator)  
[chapter 9(composite)](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/composite)  
[chapter 10(state)](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/state)  
chapter 11(proxy) (Translating this chapter is beyond my ability.)  
[chapter 12(combining)](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/combining)  
chapter 12(combined) (Translating this subsection is beyond my ability.)  
chapter 13 (No code)  
[Appendix (bridge)](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/bridge/remote)  
[Appendix (builder)](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/builder)  
[Appendix (flyweight)](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/flyweight)  
[Appendix (prototype)](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/prototype)  
[Appendix (collections)](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/collections)  
[Appendix (ducks)](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/ducks)  
[Appendix (iterenum)](https://github.com/rebuild-123/Python-Head-First-Design-Patterns/tree/main/iterenum)  

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


