from Cook import Cook
from Order import Order
from Waitress import Waitress


class Customer:
    waitress: Waitress
    cook: Cook
    o: Order
        
    def __init__(self, waitress: Waitress, cook: Cook):
        self.waitress = waitress
        self.cook = cook
        
    def createOrder(self) -> None:
        self.o = lambda: (self.cook.makeBurger(), self.cook.makeFries())
        
    def hungry(self) -> None:
        self.waitress.takeOrder(self.o)