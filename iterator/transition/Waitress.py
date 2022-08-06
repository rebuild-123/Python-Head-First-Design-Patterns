from typing import Any, Iterator, List

from Menu import Menu
from MenuItem import MenuItem


class Waitress:
    menus: List[Menu]
        
    def __init__(self, menus: List[Menu]):
        self.menus = menus
        
    def printMenu(self) -> None:
        menuIterator: Iterator[Any] = iter(self.menus)
        menu = next(menuIterator, None) # not all "menu" has the method "hasNext".
        while menu != None:
            self.printMenu_(menu.createIterator())
            menu = next(menuIterator, None)
            
    # authors' java code has two "printMenu", which cannot be translated to python.
    def printMenu_(self, iterator: Iterator[Any]) -> None:
        menuItem = next(iterator, None) # not all "iterator" has the method "hasNext".
        while menuItem != None:
            print(f"{menuItem.getName()}, ", end="")
            print(f"{menuItem.getPrice()} -- ", end="")
            print(menuItem.getDescription())
            menuItem = next(iterator, None)