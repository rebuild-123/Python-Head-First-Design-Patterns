from House import House
from HouseBuilder import HouseBuilder
from InteriorWall import InteriorWall
from Roof import Roof
from Wall import Wall
from Window import Window


class StoneHouseBuilder(HouseBuilder):
    numWalls: int = 5 # Stone houses have 5 walls: 4 exterior, 1 interior
    numWindows: int = 20 # Stone houses have a lot of windows
    windowMaterial: str = "Antique glass"
    wallMaterial: str = "Stone, 2 feet thick"
    interiorWallMaterial: str = "Stone, 1 foot thick"
    roofMaterial: str = "Tile"
    def __init__(self) -> None:
        self.builderName = "Stone House Builder"
        self.setHouseType(self.HouseType.STONE)
        self.house.name = "Stone House" # Not in the authors' code.
    def addWalls(self) -> HouseBuilder:
        # Add 4 exterior walls
        for i in range(self.numWalls-1):
            print(f"Stick stone for wall made out of {self.wallMaterial}") # Not in the authors' code.
            self.house.addWall(Wall(self.interiorWallMaterial))
        # Add 1 interior wall
        print(f"Stick stone for interior wall made out of {self.interiorWallMaterial}") # Not in the authors' code.
        self.house.addWall(InteriorWall(self.wallMaterial))
        return self
    def addWindows(self) -> HouseBuilder:
        for i in range(self.numWindows):
            print(f"Adding window made out of {self.windowMaterial}") # Not in the authors' code.
            self.house.addWindow(Window(self.windowMaterial))
        return self
    def addRoof(self) -> HouseBuilder:
        self.house.addRoof(Roof(self.roofMaterial))
        return self
    def build(self) -> House:
        print("Stick everything together with mortar")
        return self.house