from Order import Order


class Waitress:
    order: Order
    
    def __init__(self):
        pass
    
    def takeOrder(self, order: Order) -> None:
        self.order = order
        self.order.orderUp()