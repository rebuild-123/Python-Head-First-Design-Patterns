from Beverage import Beverage
from CondimentDecorator import CondimentDecorator


class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage
        
    def getDescription(self) -> str:
        return self.beverage.getDescription() + ', Whip'
    
    def cost(self) -> float:
        return 0.10 + self.beverage.cost()