from Beverage import Beverage


class Espresso(Beverage):
    def __init__(self):
        self.description = "Espresso"
    
    def cost(self) -> float:
        return 1.99