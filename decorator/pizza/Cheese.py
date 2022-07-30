from Pizza import Pizza
from ToppingDecorator import ToppingDecorator


class Cheese(ToppingDecorator):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza
        
    def getDescription(self) -> str:
        return self.pizza.getDescription() + ", Cheese"
    
    def cost(self) -> float:
        return self.pizza.cost() # cheese is free