from abc import ABC, abstractmethod
from typing import List


class Pizza(ABC):
    name: str
    dough: str
    sauce: str
    toppings: List[str]
        
    def prepare(self) -> None:
        print(f"Prepare {self.name}")
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings: ")
        for topping in self.toppings:
            print(f'   {topping}')
    
    def bake(self) -> None:
        print("Bake for 25 minutes at 350")
        
    def cut(self) -> None:
        print("Cut the pizza into diagonal slices")
        
    def box(self) -> None:
        print("Place pizza in official PizzaStore box")
        
    def getName(self) -> str:
        return self.name
    
    def toString(self) -> str:
        display: StringBuffer = StringBuffer()
        display.append(f"---- {self.name} ----\n")
        display.append(f"{self.dough}\n")
        display.append(f"{self.sauce}\n")
        for topping in self.toppings:
            display.append(f'{topping}\n')
        return display.toString()
    
class StringBuffer:
    def __init__(self):
        self.ls = []
        
    def append(self, string: str) -> None:
        self.ls.append(string)
        
    def toString(self) -> str:
        return ''.join(self.ls)