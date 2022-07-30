from Beverage import Beverage
from DarkRoast import DarkRoast
from Espresso import Espresso
from HouseBlend import HouseBlend
from Mocha import Mocha
from Soy import Soy
from Whip import Whip


class StarbuzzCoffee:
    @staticmethod
    def main(*args) -> None:
        beverage: Beverage = Espresso()
        print(f'{beverage.getDescription()} ${beverage.cost()}')
        
        beverage2: Beverage = DarkRoast()
        beverage2 = Mocha(beverage2)
        beverage2 = Mocha(beverage2)
        beverage2 = Whip(beverage2)
        print(f'{beverage2.getDescription()} ${beverage2.cost()}')
        
        beverage3: Beverage = HouseBlend()
        beverage3 = Soy(beverage3)
        beverage3 = Mocha(beverage3)
        beverage3 = Whip(beverage3)
        print(f'{beverage3.getDescription()} ${beverage3.cost()}')
        
if __name__ == "__main__":
    StarbuzzCoffee.main()