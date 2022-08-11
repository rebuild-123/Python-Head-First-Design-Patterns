from PizzaBuilder import PizzaBuilder


class MeatLoversPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.name = "Meat Lovers Pizza"
        self.toppings = [] # Not in the authors' code.
    def addCheese(self) -> PizzaBuilder:
        # meat lovers like moz
        self.toppings.append("mozzerella")
        return self
    def addSauce(self) -> PizzaBuilder:
        self.toppings.append("NY style sauce")
        return self
    def addTomatoes(self) -> PizzaBuilder:
        self.toppings.append("sliced tomatoes")
        return self
    def addGarlic(self) -> PizzaBuilder:
        self.toppings.append("garlic")
        return self
    def addOlives(self) -> PizzaBuilder:
        # never add olives to meat lovers pizza
        return self
    def addSpinach(self) -> PizzaBuilder:
        # never add spinach to meat lovers pizza
        return self
    def addPepperoni(self) -> PizzaBuilder:
        self.toppings.append("pepperoni")
        return self
    def addSausage(self) -> PizzaBuilder:
        self.toppings.append("sausage")
        return self