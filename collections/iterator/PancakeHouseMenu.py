from typing import Iterator, List

from Menu import Menu
from PancakeHouseMenuIterator import PancakeHouseMenuIterator


class PancakeHouseMenu(Menu):
    menuItems: List[str]
        
    def __init__(self):
        self.menuItems = []
        
        self.addItem("K&B's Pancake Breakfast")
        self.addItem("Regular Pancake Breakfast")
        self.addItem("Blueberry Pancakes")
        self.addItem("Waffles")
        
    def addItem(self, name: str) -> None:
        self.menuItems.append(name)
            
    def getMenuItems(self) -> List[str]:
        return self.menuItems
    
    def createIterator(self) -> Iterator[str]:
        return PancakeHouseMenuIterator(self.menuItems)
    
    # toString
    def __str__(self) -> str:
        return "Pancake House Menu"
    
    # toString
    def __repr__(self) -> str:
        return str(self)
    
    # other menu methods here