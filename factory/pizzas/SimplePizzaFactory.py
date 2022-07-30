from CheesePizza import CheesePizza
from ClamPizza import ClamPizza
from PepperoniPizza import PepperoniPizza
from Pizza import Pizza
from VeggiePizza import VeggiePizza


class SimplePizzaFactory:
    def createPizza(self, type_: str) -> Pizza:
        pizza: Pizza = None
        if type_ == "cheese":
            pizza = CheesePizza()
        elif type_ == "pepperoni":
            pizza = PepperoniPizza()
        elif type_ == "clam":
            pizza = ClamPizza()
        elif type_ == "veggie":
            pizza = VeggiePizza()
        return pizza