from typing import Iterator

from MenuComponent import MenuComponent


class UnsupportedOperationException(Exception): pass

class Waitress:
    allMenus: MenuComponent
        
    def __init__(self, allMenus: MenuComponent):
        self.allMenus = allMenus
        
    def printMenu(self) -> None:
        self.allMenus.print()
        
    def printVegetarianMenu(self) -> None:
        iterator: Iterator[MenuComponent] = self.allMenus.createIterator()
            
        print("\nVEGETARIAN MENU\n----")
        menuComponent: MenuComponent = next(iterator, None)
        while menuComponent != None:
            try:
                if menuComponent.isVegetarian():
                    menuComponent.print()
            except:
                # raise UnsupportedOperationException
                pass
            menuComponent: MenuComponent = next(iterator, None)