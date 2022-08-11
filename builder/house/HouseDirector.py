# from ClayHouseBuilder import ClayHouseBuilder # there is no "ClayHouseBuilder" in authors' code.
from GingerbreadHouseBuilder import GingerbreadHouseBuilder
from House import House
from HouseBuilder import HouseBuilder
from StoneHouseBuilder import StoneHouseBuilder
from WoodHouseBuilder import WoodHouseBuilder


class HouseDirector:
    
    # Fluent Interface pattern (return the builder each time so we can string the calls together)
    # Builder pattern (we have two different builders so the "same construction process can create
    #   different representations").
    # Builder is a solution to the telescoping constructor anti-pattern, where we have multiple,
    #   complex constructor methods with various args for all various combinations of options
    #   in construction options. 

    # in this example main() is the construct() method
    @staticmethod
    def main(*args) -> None:
        # The Director calls the methods in the correct order to build a house. 
        # Could make this a lot more complicated to allow number of walls, windows, to be passed in.
        
        woodHouseBuilder: HouseBuilder = WoodHouseBuilder()
        woodHouse: House = woodHouseBuilder.addWalls().addWindows().addRoof().build()
        print(woodHouse)
        
        # there is no "ClayHouseBuilder" in authors' code.
        # clayHouseBuilder: HouseBuilder = ClayHouseBuilder()
        # clayHouse: House = clayHouseBuilder.addWalls().addWindows().addRoof().build()
        # print(clayHouse)
        
        stoneHouseBuilder: HouseBuilder = StoneHouseBuilder()
        stoneHouse: House = stoneHouseBuilder.addWalls().addWindows().addRoof().build()
        print(stoneHouse)
        
        gingerbreadHouseBuilder: HouseBuilder = GingerbreadHouseBuilder()
        gingerbreadHouse: House = gingerbreadHouseBuilder.addWalls().addWindows().addRoof().build()
        print(gingerbreadHouse)
        
        # Builder has similarities to Abstract Factory.
        # But difference is that Builder provides a step by step API for building a product;
        #   the client is responsible for calling the steps, and those can vary in order, etc.
        #   With Builder, the client must have more knowledge of the details of the product being built.
        # Product implementations can be swapped for others; clients don't change because the use the abstract API.
        
if __name__ == "__main__":
    HouseDirector.main()