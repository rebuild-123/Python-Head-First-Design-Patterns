from Pizza import Pizza
from ToppingDecorator import ToppingDecorator


class Olives(ToppingDecorator):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza
        
    def getDescription(self) -> str:
        return self.pizza.getDescription() + ", Olives"
    
    def cost(self) -> float:
        return self.pizza.cost() + 0.30