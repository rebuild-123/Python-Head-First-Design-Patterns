from typing import Iterator, List

from DinerMenu import DinerMenu
from PancakeHouseMenu import PancakeHouseMenu


class Cafe:
    @staticmethod
    def main(*args) -> None:
        pancakeHouseMenu: PancakeHouseMenu = PancakeHouseMenu()
        dinerMenu: DinerMenu = DinerMenu()
            
        # with iterators
        pancakeIterator: Iterator = pancakeHouseMenu.createIterator()
        dinerIterator: Iterator = dinerMenu.createIterator()
            
        print("\nMENU (with iterators)\n----\nBREAKFAST")
        Cafe.printMenu(pancakeIterator)
        print("\nLUNCH")
        Cafe.printMenu(dinerIterator)
        
    @staticmethod
    def printMenu(iterator: Iterator) -> None:
        menuItem: str = next(iterator, None)
        while menuItem != None:
            print(menuItem)
            menuItem: str = next(iterator, None)
            
if __name__ == "__main__":
    Cafe.main()