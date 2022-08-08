from typing import Iterator

from MenuComponent import MenuComponent


class MenuItem:
    name: str
    description: str
    vegetarian: bool
    price: float
        
    def __init__(self, name: str, description: str, vegetarian: bool, price: float):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price
        
    def getName(self) -> str:
        return self.name
    
    def getDescription(self) -> str:
        return self.description
    
    def getPrice(self) -> float:
        return self.price
    
    def isVegetarian(self) -> bool:
        return self.vegetarian
    
    def createIterator(self) -> Iterator[MenuComponent]:
        return NullIterator()
    
    def print(self) -> None:
        print(f"  {self.getName()}", end="")
        if self.isVegetarian():
            print(f"(v)", end="")
        print(f", {self.getPrice()}")
        print(f"     -- {self.getDescription()}")