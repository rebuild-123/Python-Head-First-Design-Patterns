from PizzaBuilder import PizzaBuilder


class VeggieLoversPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.name = "Veggie Lovers Pizza"
        self.toppings = [] # Not in the authors' code.
    def addCheese(self) -> PizzaBuilder:
        # veggie lovers like parm
        self.toppings.append("parmesan")
        return self
    def addSauce(self) -> PizzaBuilder:
        self.toppings.append("sauce")
        return self
    def addTomatoes(self) -> PizzaBuilder:
        self.toppings.append("chopped tomatoes")
        return self
    def addGarlic(self) -> PizzaBuilder:
        self.toppings.append("garlic")
        return self
    def addOlives(self) -> PizzaBuilder:
        self.toppings.append("green olives")
        return self
    def addSpinach(self) -> PizzaBuilder:
        self.toppings.append("spinach")
        return self
    def addPepperoni(self) -> PizzaBuilder:
        # ever EVER add Pepperoni to veggie lovers pizza
        return self
    def addSausage(self) -> PizzaBuilder:
        # never EVER add Sausage to veggie lovers pizza
        return self