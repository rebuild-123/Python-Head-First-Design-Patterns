from typing import Final, Iterator, List

from DinerMenuIterator import DinerMenuIterator
from Menu import Menu


class DinerMenu(Menu):
    MAX_ITEMS: Final[int] = 6
    numberOfItems: int = 0
    menuItems: List[str]
        
    def __init__(self):
        self.menuItems = []
        
        self.addItem("Vegetarian BLT")
        self.addItem("BLT")
        self.addItem("Hotdog")
        self.addItem("Steamed Veggies and Brown Rice")
        self.addItem("Pasta")
        
    def addItem(self, name: str) -> None:
        if self.numberOfItems >= self.MAX_ITEMS:
            print("Sorry, menu is full!  Can't add item to menu")
        else:
            self.menuItems.append(name)
            self.numberOfItems += 1
            
    def getMenuItems(self) -> List[str]:
        return self.menuItems
    
    def createIterator(self) -> Iterator[str]:
        return DinerMenuIterator(self.menuItems)
    
    # toString
    def __str__(self) -> str:
        return "Diner Menu"
    
    # toString for print
    def __repr__(self) -> str:
        return str(self)