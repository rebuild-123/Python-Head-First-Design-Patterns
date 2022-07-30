from ChicagoStyleCheesePizza import ChicagoStyleCheesePizza
from ChicagoStyleClamPizza import ChicagoStyleClamPizza
from ChicagoStylePepperoniPizza import ChicagoStylePepperoniPizza
from ChicagoStyleVeggiePizza import ChicagoStyleVeggiePizza
from Pizza import Pizza
from PizzaStore import PizzaStore


class ChicagoPizzaStore(PizzaStore):
    def createPizza(self, item: str) -> Pizza:
        if item == "cheese":
            return ChicagoStyleCheesePizza()
        elif item == "veggie":
            return ChicagoStyleVeggiePizza()
        elif item == "clam":
            return ChicagoStyleClamPizza()
        elif item == "pepperoni":
            return ChicagoStylePepperoniPizza()
        else:
            return None