from typing import Dict, Iterator

from Menu import Menu
from MenuItem import MenuItem

class CafeMenu(Menu):
    menuItems: Dict[str, MenuItem] = dict()
        
    def __init__(self):
        self.addItem("Veggie Burger and Air Fries",
                     "Veggie burger on a whole wheat bun, lettuce, tomato, and fries",
                     True, 3.99);
        self.addItem("Soup of the day",
                     "A cup of the soup of the day, with a side salad",
                     False, 3.69);
        self.addItem("Burrito",
                     "A large burrito, with whole pinto beans, salsa, guacamole",
                     True, 4.29)
        
    def addItem(self, name: str, description: str, vegetarian: bool, price: float) -> None:
        menuItem: MenuItem = MenuItem(name, description, vegetarian, price)
        self.menuItems[name] = menuItem
        
    def getItems(self) -> Dict[str, MenuItem]:
        return self.menuItems
    
    def createIterator(self) -> Iterator[MenuItem]:
        return iter(self.menuItems.values())