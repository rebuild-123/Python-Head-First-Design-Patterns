from typing import List

from DinerMenu import DinerMenu
from Menu import Menu
from PancakeHouseMenu import PancakeHouseMenu
from Waitress import Waitress


class MenuTestDrive:
    @staticmethod
    def main(*args):
        pancakeHouseMenu: PancakeHouseMenu = PancakeHouseMenu()
        dinerMenu: DinerMenu = DinerMenu()
        menus: List[Menu] = []
        menus.append(pancakeHouseMenu)
        menus.append(dinerMenu)
        waitress: Waitress = Waitress(menus)
        waitress.printMenu()
        
if __name__ == "__main__":
    MenuTestDrive.main()