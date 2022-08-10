from typing import List

from DinerMenu import DinerMenu
from Iterator import Iterator
from PancakeHouseMenu import PancakeHouseMenu


class Cafe:
    @staticmethod
    def main(*args) -> None:
        pancakeHouseMenu: PancakeHouseMenu = PancakeHouseMenu()
        dinerMenu: DinerMenu = DinerMenu()
            
        # with no iterators
        print("\nMENU\n----\nBREAKFAST")
        breakfastItems: List[str] = pancakeHouseMenu.getMenuItems()
        for i in range(len(breakfastItems)):
            menuItem: str = breakfastItems[i]
            print(menuItem)
            
        print("\nLUNCH")
        lunchItems: List[str] = dinerMenu.getMenuItems()
        for i in range(len(lunchItems)):
            menuItem: str = lunchItems[i]
            print(menuItem)
            
        # with iterators
        pancakeIterator: Iterator = pancakeHouseMenu.createIterator()
        dinerIterator: Iterator = dinerMenu.createIterator()
            
        print("\nMENU (with iterators)\n----\nBREAKFAST")
        Cafe.printMenu(pancakeIterator)
        print("\nLUNCH")
        Cafe.printMenu(dinerIterator)
        
    @staticmethod
    def printMenu(iterator: Iterator) -> None:
        while iterator.hasNext():
            menuItem: str = next(iterator, None)
            print(menuItem)
            
if __name__ == "__main__":
    Cafe.main()