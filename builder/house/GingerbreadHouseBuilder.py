from House import House
from HouseBuilder import HouseBuilder
from InteriorWall import InteriorWall
from Roof import Roof
from Wall import Wall
from Window import Window


class GingerbreadHouseBuilder(HouseBuilder):
    numWalls: int = 4
    numWindows: int = 4
    windowMaterial: str = "Sugar"
    wallMaterial: str = "Gingerbread and icing"
    roofMaterial: str = "Twizzlers"
    def __init__(self) -> None:
        self.builderName = "Gingerbread House Builder"
        self.setHouseType(self.HouseType.GINGERBREAD)
        self.house.name = "Gingerbread House" # Not in the authors' code.
    def addWalls(self) -> HouseBuilder:
        # add exterior walls
        for i in range(4):
            print(f"Adding wall made out of {self.wallMaterial}")
            self.house.addWall(Wall(self.wallMaterial))
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
        print("Stick everything together with icing")
        return self.house