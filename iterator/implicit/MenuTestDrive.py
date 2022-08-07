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
        waitress: Waitress = Waitress(pancakeHouseMenu, dinerMenu)
        # Use implicit iteration
        waitress.printMenu()
        
if __name__ == "__main__":
    MenuTestDrive.main()