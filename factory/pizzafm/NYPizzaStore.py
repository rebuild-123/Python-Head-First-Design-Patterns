from NYStyleCheesePizza import NYStyleCheesePizza
from NYStyleClamPizza import NYStyleClamPizza
from NYStylePepperoniPizza import NYStylePepperoniPizza
from NYStyleVeggiePizza import NYStyleVeggiePizza
from Pizza import Pizza
from PizzaStore import PizzaStore


class NYPizzaStore(PizzaStore):
    def createPizza(self, item: str) -> Pizza:
        if item == "cheese":
            return NYStyleCheesePizza()
        elif item == "veggie":
            return NYStyleVeggiePizza()
        elif item == "clam":
            return NYStyleClamPizza()
        elif item == "pepperoni":
            return NYStylePepperoniPizza()
        else:
            return None