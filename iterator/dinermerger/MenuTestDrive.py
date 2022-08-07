from typing import Iterable, List

from DinerMenu import DinerMenu
from Menu import Menu
from MenuItem import MenuItem
from PancakeHouseMenu import PancakeHouseMenu
from Waitress import Waitress


class MenuTestDrive:
    @staticmethod
    def main(*args) -> None:
        pancakeHouseMenu: Menu = PancakeHouseMenu()
        dinerMenu: Menu = DinerMenu()
        waitress: Waitress = Waitress(pancakeHouseMenu, dinerMenu)
        # With iterators
        waitress.printMenu()
        print('\n--------------------------------------------------------\n')
        MenuTestDrive.printMenus()
        
    # Without the Waitress, we need the code below...
    @staticmethod
    def printMenus() -> None:
        pancakeHouseMenu: PancakeHouseMenu = PancakeHouseMenu()
        dinerMenu: DinerMenu = DinerMenu()
            
        breakfastItems: List[MenuItem] = pancakeHouseMenu.getMenuItems()
        lunchItems: List[MenuItem] = dinerMenu.getMenuItems()
            
        # print as Iterable
        MenuTestDrive.printMenu(breakfastItems)
        MenuTestDrive.printMenu(lunchItems)
        
        # print with forEach
        print("=== forEach ===")
        for item in breakfastItems: print(item)
        for item in lunchItems: print(item)
        print("=== forEach ===")
        
        # Using enhanced for loop
        print("USING ENHANCED FOR")
        for menuItem in breakfastItems:
            print(menuItem.getName(), end="")
            print(f"\t\t{menuItem.getPrice()}")
            print(f"\t{menuItem.getDescription()}")
        for menuItem in lunchItems:
            print(menuItem.getName(), end="")
            print(f"\t\t{menuItem.getPrice()}")
            print(f"\t{menuItem.getDescription()}")
            
        # Exposing implementation
        print("USING FOR LOOPS")
        for i in range(len(breakfastItems)):
            menuItem: MenuItem = breakfastItems[i]
            print(menuItem.getName(), end="")
            print(f"\t\t{menuItem.getPrice()}")
            print(f"\t{menuItem.getDescription()}")
            
        for i in range(len(lunchItems)):
            menuItem: MenuItem = lunchItems[i]
            print(menuItem.getName(), end="")
            print(f"\t\t{menuItem.getPrice()}")
            print(f"\t{menuItem.getDescription()}")
        
    @staticmethod
    def printMenu(a: Iterable[MenuItem] = []):
        for menuItem in a:
            print(menuItem.getName(), end="")
            print(f"\t\t{menuItem.getPrice()}")
            print(f"\t{menuItem.getDescription()}")
            
if __name__ == "__main__":
    MenuTestDrive.main()