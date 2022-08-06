from typing import Final, Iterator, List

from DinerMenuIterator import DinerMenuIterator
from Menu import Menu
from MenuItem import MenuItem


class DinerMenu(Menu):
    MAX_ITEMS: Final[int] = 6
    numberOfItems: int = 0
    menuItems: List[MenuItem]
        
    def __init__(self):
        self.menuItems = []
        
        self.addItem("Vegetarian BLT","(Fakin') Bacon with lettuce & tomato on whole wheat", True, 2.99)
        self.addItem("BLT","Bacon with lettuce & tomato on whole wheat", False, 2.99)
        self.addItem("Soup of the day","Soup of the day, with a side of potato salad", False, 3.29)
        self.addItem("Hotdog","A hot dog, with sauerkraut, relish, onions, topped with cheese",False, 3.05)
        self.addItem("Steamed Veggies and Brown Rice","Steamed vegetables over brown rice", True, 3.99)
        self.addItem("Pasta","Spaghetti with Marinara Sauce, and a slice of sourdough bread",True, 3.89)
        
    def addItem(self, name: str, description: str, vegetarian: bool, price: float) -> None:
        menuItem: MenuItem = MenuItem(name, description, vegetarian, price)
        if self.numberOfItems >= self.MAX_ITEMS:
            print("Sorry, menu is full!  Can't add item to menu")
        else:
            self.menuItems.append(menuItem)
            self.numberOfItems += 1
            
    def getMenuItems(self) -> List[MenuItem]:
        return self.menuItems
    
    def createIterator(self) -> Iterator[MenuItem]:
        return DinerMenuIterator(self.menuItems)
        # return AlternatingDinerMenuIterator(menuItems)
    
    # other menu methods here