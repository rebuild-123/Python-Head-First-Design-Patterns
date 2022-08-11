from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum

from House import House


class HouseBuilder(ABC):
    builderName: str
    HouseType: Enum = Enum('HouseType', 'WOOD CLAY GINGERBREAD STONE')
    houseType: HouseType
    house: House = House()
        
    def setHouseType(self, houseType: HouseType) -> None:
        self.houseType = houseType
        self.house.setHouseType(houseType)
    # Each method in the Builder returns the Builder so we can use the Fluent Interface Pattern
    @abstractmethod
    def addWalls(self) -> HouseBuilder:
        pass
    @abstractmethod
    def addRoof(self) -> HouseBuilder:
        pass
    @abstractmethod
    def addWindows(self) -> HouseBuilder:
        pass
    
    def build(self) -> House:
        print("Build the house!")
        # Very simple build -- just return the house!
        # We've added all the parts... 
        # In a real build, we'd have to nail and screw everything together of course.
        # And add wiring and so on.
        return self.house