from abc import ABC, abstractmethod
from typing import List

from Cheese import Cheese
from Clams import Clams
from Dough import Dough
from Pepperoni import Pepperoni
from Sauce import Sauce
from Veggies import Veggies


class Pizza(ABC):
    name: str = None
    dough: Dough = None
    sauce: Sauce = None
    veggies: List[Veggies] = None
    cheese: Cheese = None
    pepperoni: Pepperoni = None
    clam: Clams = None
        
    @abstractmethod
    def prepare(self) -> None:
        raise NotImplementedError
        
    def bake(self) -> None:
        print("Bake for 25 minutes at 350")
        
    def cut(self) -> None:
        print("Cutting the pizza into diagonal slices")
        
    def box(self) -> None:
        print("Place pizza in official PizzaStore box")
        
    def setName(self, name: str) -> None:
        self.name = name
        
    def getName(self) -> str:
        return self.name
    
    def toString(self) -> str:
        result: StringBuffer = StringBuffer()
        result.append(f"---- {self.name} ----\n")
        if self.dough != None:
            result.append(self.dough.toString())
            result.append('\n')
        if self.sauce != None:
            result.append(self.sauce.toString())
            result.append('\n')
        if self.cheese != None:
            result.append(self.cheese.toString())
            result.append('\n')
        if self.veggies != None and self.veggies:
            for i in range(len(self.veggies)):
                result.append(self.veggies[i].toString())
                if i < len(self.veggies) - 1:
                    result.append(', ')
            result.append('\n')
        if self.clam != None:
            result.append(self.clam.toString())
            result.append('\n')
        if self.pepperoni != None:
            result.append(self.pepperoni.toString())
            result.append('\n')
        return result.toString()
    
class StringBuffer:
    def __init__(self):
        self.ls = []
        
    def append(self, string: str) -> None:
        self.ls.append(string)
        
    def toString(self) -> str:
        return ''.join(self.ls)