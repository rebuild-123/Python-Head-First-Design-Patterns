from Cook import Cook
from Order import Order


class BurgerAndFriesOrder(Order):
    cook: Cook
    
    def __init__(self, cook: Cook):
        self.cook = cook
        
    def orderUp(self) -> None:
        self.cook.makeBurger()
        self.cook.makeFries()