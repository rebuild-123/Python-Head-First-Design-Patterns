from typing import Iterator

from CafeMenu import CafeMenu
from Menu import Menu
from MenuItem import MenuItem


class Waitress:
    pancakeHouseMenu: Menu
    dinerMenu: Menu
    cafeMenu: Menu
        
    def __init__(self, pancakeHouseMenu: Menu, dinerMenu: Menu, cafeMenu: Menu):
        self.pancakeHouseMenu = pancakeHouseMenu
        self.dinerMenu = dinerMenu
        self.cafeMenu = cafeMenu
        
    def printMenu(self) -> None:
        pancakeIterator: Iterator = self.pancakeHouseMenu.createIterator()
        dinerIterator: Iterator = self.dinerMenu.createIterator()
        cafeIterator: Iterator = self.cafeMenu.createIterator()
            
        print('MENU\n----\nBREAKFAST')
        self.printMenu_(pancakeIterator)
        print("\nLUNCH")
        self.printMenu_(dinerIterator)
        print("\nDINNER")
        self.printMenu_(cafeIterator)
        
    # authors' java code has two "printMenu", which cannot be translated to python.
    def printMenu_(self, iterator: Iterator) -> None:
        menuItem: MenuItem = next(iterator, None) # not all "iterator" has the method "hasNext".
        while menuItem != None:
            print(f'{menuItem.getName()}, ', end="")
            print(f'{menuItem.getPrice()} -- ', end="")
            print(menuItem.getDescription())
            menuItem: MenuItem = next(iterator, None)
            
    def printVegetarianMenu(self) -> None:
        print("\nVEGETARIAN MENU\n---------------")
        self.printVegetarianMenu_(self.pancakeHouseMenu.createIterator())
        self.printVegetarianMenu_(self.dinerMenu.createIterator())
        self.printVegetarianMenu_(self.cafeMenu.createIterator())
        
    def isItemVegetarian(self, name: str) -> bool:
        breakfastIterator: Iterator = self.pancakeHouseMenu.createIterator()
        if self.isVegetarian(name, breakfastIterator):
            return True
        dinnerIterator: Iterator = self.dinerMenu.createIterator()
        if self.isVegetarian(name, dinnerIterator):
            return True
        cafeIterator: Iterator = self.cafeMenu.createIterator()
        if self.isVegetarian(name, cafeIterator):
            return True
        return False
    
    # authors' java code has two "printVegetarianMenu", which cannot be translated to python.
    def printVegetarianMenu_(self, iterator: Iterator) -> None:
        menuItem: MenuItem = next(iterator, None) # not all "iterator" has the method "hasNext".
        while menuItem != None:
            if menuItem.isVegetarian():
                print(f"{menuItem.getName()}, ", end="")
                print(f"{menuItem.getPrice()} -- ", end="")
                print(f"{menuItem.getDescription()}")
            menuItem: MenuItem = next(iterator, None)
                
    def isVegetarian(self, name: str, iterator: Iterator) -> bool:
        menuItem: MenuItem = next(iterator, None) # not all "iterator" has the method "hasNext".
        while menuItem != None:
            if menuItem.getName() == name:
                if menuItem.isVegetarian():
                    return True
            menuItem: MenuItem = next(iterator, None)
        return False