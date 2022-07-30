from Beverage import Beverage
from CondimentDecorator import CondimentDecorator


class Milk(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage
        
    def getDescription(self) -> str:
        return self.beverage.getDescription() + ', Milk'
    
    def cost(self) -> float:
        return 0.10 + self.beverage.cost()