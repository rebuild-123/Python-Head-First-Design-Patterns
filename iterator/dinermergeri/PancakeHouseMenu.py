from typing import Iterator, List

from Menu import Menu
from MenuItem import MenuItem


class PancakeHouseMenu(Menu):
    menuItems: List[MenuItem]
        
    def __init__(self):
        self.menuItems = []
        
        self.addItem("K&B's Pancake Breakfast", "Pancakes with scrambled eggs and toast", True,2.99)
        self.addItem("Regular Pancake Breakfast", "Pancakes with fried eggs, sausage", False,2.99)
        self.addItem("Blueberry Pancakes","Pancakes made with fresh blueberries and blueberry syrup",True,3.49)
        self.addItem("Waffles","Waffles with your choice of blueberries or strawberries",True,3.59)
        
    def addItem(self, name: str, description: str, vegetarian: bool, price: float) -> None:
        menuItem: MenuItem = MenuItem(name, description, vegetarian, price)
        self.menuItems.append(menuItem)
            
    def getMenuItems(self) -> List[MenuItem]:
        return self.menuItems
    
    def createIterator(self) -> Iterator[MenuItem]:
        return iter(self.menuItems)
    
    # other menu methods here