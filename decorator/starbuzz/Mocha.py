from Beverage import Beverage
from CondimentDecorator import CondimentDecorator


class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage
        
    def getDescription(self) -> str:
        return self.beverage.getDescription() + ', Mocha'
    
    def cost(self) -> float:
        return 0.20 + self.beverage.cost()