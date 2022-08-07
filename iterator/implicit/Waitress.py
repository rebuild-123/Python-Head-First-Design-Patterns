from typing import List

from Menu import Menu
from MenuItem import MenuItem


class Waitress:
    pancakeHouseMenu: Menu
    dinerMenu: Menu
        
    def __init__(self, pancakeHouseMenu: Menu, dinerMenu: Menu):
        self.pancakeHouseMenu = pancakeHouseMenu
        self.dinerMenu = dinerMenu
        
    # implicit iteration
    def printMenu(self) -> None:
        breakfastItems: List[MenuItem] = self.pancakeHouseMenu.getMenuItems()
        for m in breakfastItems:
            self.printMenuItem(m)
            
        lunchItems: List[MenuItem] = self.dinerMenu.getMenuItems()
        for m in lunchItems:
            self.printMenuItem(m)
            
    def printMenuItem(self, menuItem: MenuItem) -> None:
        print(f"{menuItem.getName()}, ", end="")
        print(f"{menuItem.getPrice()} -- ", end="")
        print(menuItem.getDescription())