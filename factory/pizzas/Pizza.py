from abc import ABC, abstractmethod
from typing import List


class Pizza(ABC):
    name: str
    dough: str
    sauce: str
    toppings: List[str]
    
    def getName(self) -> str:
        return self.name
    
    def prepare(self) -> None:
        print(f'Preparing {self.name}')
        
    def bake(self) -> None:
        print(f'Baking {self.name}')
        
    def cut(self) -> None:
        print(f'Cutting {self.name}')
        
    def box(self) -> None:
        print(f'Boxing {self.name}')
        
    def toString(self) -> str:
        # code to display pizza name and ingredients
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