from collections import UserList
from typing import Iterator, List

from CompositeIterator import CompositeIterator
from MenuComponent import MenuComponent


class My_List(UserList): 
    def __init__(self, data):
        super().__init__(data)
        self.position = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.hasNext():
            num = self.data[self.position]
            self.position += 1
            return num
        else:
            raise StopIteration
            
    def hasNext(self):
        if self.position >= len(self.data):
            self.position = 0
            return False
        else:
            return True

class Menu(MenuComponent):
    iterator: Iterator[MenuComponent] = None
    menuComponents: List[MenuComponent]
    name: str
    description: str
        
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.menuComponents = My_List([])
        
    def add(self, menuComponent: MenuComponent) -> None:
        self.menuComponents.append(menuComponent)
        
    def remove(self, menuComponent: MenuComponent) -> None:
        self.menuComponents.remove(menuComponent)
        
    def getChild(self, i: int) -> MenuComponent:
        return self.menuComponents[i]
    
    def getName(self) -> str:
        return self.name
    
    def getDescription(self) -> str:
        return self.description
    
    def createIterator(self) -> Iterator[MenuComponent]:
        if self.iterator == None:
            self.iterator = CompositeIterator(iter(self.menuComponents))
        return self.iterator
    
    def print(self) -> None:
        print(f'\n{self.getName()}', end="")
        print(f", {self.getDescription()}")
        print("---------------------")
        
        iterator: Iterator[MenuComponent] = iter(self.menuComponents)
        menuComponent: MenuComponent = next(iterator, None)
        while menuComponent != None:
            menuComponent.print()
            menuComponent: MenuComponent = next(iterator, None)