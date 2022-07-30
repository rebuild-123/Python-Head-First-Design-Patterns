from Beverage import Beverage
from CondimentDecorator import CondimentDecorator


class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage
        
    def getDescription(self) -> str:
        return self.beverage.getDescription() + ', Soy'
    
    def cost(self) -> float:
        return 0.15 + self.beverage.cost()