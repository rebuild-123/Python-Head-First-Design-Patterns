from typing import Iterable, List

from CafeMenu import CafeMenu
from DinerMenu import DinerMenu
from Menu import Menu
from MenuItem import MenuItem
from PancakeHouseMenu import PancakeHouseMenu
from Waitress import Waitress


class MenuTestDrive:
    @staticmethod
    def main(*args) -> None:
        pancakeHouseMenu: PancakeHouseMenu = PancakeHouseMenu()
        dinerMenu: DinerMenu = DinerMenu()
        cafeMenu: CafeMenu = CafeMenu()
        waitress: Waitress = Waitress(pancakeHouseMenu, dinerMenu, cafeMenu)
        
        waitress.printMenu()
        waitress.printVegetarianMenu()
        
        print("\nCustomer asks, is the Hotdog vegetarian?")
        print("Waitress says: ", end="")
        if waitress.isItemVegetarian("Hotdog"):
            print('Yes')
        else:
            print('No')
        print("\nCustomer asks, are the Waffles vegetarian?")
        print("Waitress says: ", end="")
        if waitress.isItemVegetarian("Waffles"):
            print('Yes')
        else:
            print('No')
            
if __name__ == "__main__":
    MenuTestDrive.main()