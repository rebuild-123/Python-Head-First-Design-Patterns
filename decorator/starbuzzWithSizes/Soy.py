from Beverage import Beverage
from CondimentDecorator import CondimentDecorator


class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage
        
    def getDescription(self) -> str:
        return self.beverage.getDescription() + ', Soy'
    
    def cost(self) -> float:
        cost: float = self.beverage.cost()
        if self.beverage.getSize() == self.Size.TALL:
            cost += 0.10
        elif self.beverage.getSize() == self.Size.GRANDE:
            cost += 0.15
        elif self.beverage.getSize() == self.Size.VENTI:
            cost += 0.20
        return cost