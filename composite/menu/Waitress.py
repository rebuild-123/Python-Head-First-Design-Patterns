from typing import Iterator

from MenuComponent import MenuComponent


class UnsupportedOperationException(Exception): pass

class Waitress:
    allMenus: MenuComponent
        
    def __init__(self, allMenus: MenuComponent):
        self.allMenus = allMenus
        
    def printMenu(self) -> None:
        self.allMenus.print()