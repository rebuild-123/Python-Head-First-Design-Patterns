from __future__ import annotations
from enum import auto, Enum
from typing import List

from Roof import Roof
from Wall import Wall
from Window import Window


class StringBuilder:
    def __init__(self):
        self.ls = []
        
    def append(self, string: str) -> None:
        self.ls.append(string)
        
    def toString(self) -> str:
        return ''.join(self.ls)

class HouseType(Enum):
    WOOD = auto()
    CLAY = auto()
    GINGERBREAD = auto()
    STONE = auto()
    
class House:
    name: str
    houseType: HouseType
    roof: Roof
    walls: List[Wall]
    windows: List[Window]
        
    def __init__(self):
        self.walls = []
        self.windows = []
        
    def setHouseType(self, houseType: HouseType) -> House:
        self.houseType = houseType
        if self.houseType == HouseType.WOOD: self.name = "My wood house"
        elif self.houseType == HouseType.CLAY: self.name = "My clay house"
        elif self.houseType == HouseType.GINGERBREAD: self.name = "My holiday gingerbread house"
        elif self.houseType == HouseType.STONE: self.name = "My stone house"
        return self
    
    def addRoof(self, roof: Roof) -> House:
        self.roof = roof
        return self
    
    def addWall(self, wall: Wall) -> House:
        self.walls.append(wall)
        return self
    
    def addWindow(self, window: Window) -> House:
        self.windows.append(window)
        return self
    
    def setName(self, name: str) -> None:
        self.name = name
        
    # toString
    def __str__(self) -> str:
        # Use a StringBuilder to build the string :-)
        # Like StringBuffer, but not synchronized
        display: StringBuilder = StringBuilder()
        display.append(f"---- {self.name} ----\n")
        for wall in self.walls:
            display.append(f"--- {wall.name} ---\n")
        for window in self.windows:
            display.append(f"--- {window.name} ---\n")
        display.append(f"--- {self.roof.name} ---\n")
        return display.toString()
    
        # There is some difference of opinion about StringBuilder and whether it's using
        # the Builder pattern or not. Some say yes, some say no.
        # StringBuilder does not provide an abstract API with multiple subclasses for
        # creating different representations (variations).
        
    # toString for print
    def __repr__(self) -> str:
        return str(self)