from Order import Order
from Waitress import Waitress


class Customer:
    waitress: Waitress
    order: Order
        
    def __init__(self, waitress: Waitress):
        self.waitress = waitress
        
    def createOrder(self, order: Order) -> None:
        self.order = order
        
    def hungry(self) -> None:
        self.waitress.takeOrder(self.order)