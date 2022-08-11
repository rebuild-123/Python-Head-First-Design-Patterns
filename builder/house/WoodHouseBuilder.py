from House import House
from HouseBuilder import HouseBuilder
from InteriorWall import InteriorWall
from Roof import Roof
from Wall import Wall
from Window import Window


class WoodHouseBuilder(HouseBuilder):
    numWalls: int = 6 # 4 exterior walls, 2 interior
    numWindows: int = 10
    windowMaterial: str = "Tempered glass"
    wallMaterial: str = "Wood, 4x6"
    interiorWallMaterial: str = "Wood, 2x4"
    roofMaterial: str = "Metal"
    def __init__(self) -> None:
        self.builderName = "Wood House Builder"
        self.setHouseType(self.HouseType.WOOD)
        self.house.name = "Wood House" # Not in the authors' code.
    def addWalls(self) -> HouseBuilder:
        # add exterior walls
        for i in range(4):
            print(f"Nailing wood for wall made out of {self.wallMaterial}")
            self.house.addWall(Wall(self.wallMaterial))
        # add interior walls
        for i in range(self.numWalls - 4):
            print(f"Nailing wood for interior wall made out of {self.interiorWallMaterial}")
            self.house.addWall(InteriorWall(self.interiorWallMaterial))
        return self
    def addWindows(self) -> HouseBuilder:
        for i in range(self.numWindows):
            print(f"Adding window made out of {self.windowMaterial}")
            self.house.addWindow(Window(self.windowMaterial))
        return self
    def addRoof(self) -> HouseBuilder:
        self.house.addRoof(Roof(self.roofMaterial))
        return self
    def build(self) -> House:
        print("Nail everything together")
        return self.house