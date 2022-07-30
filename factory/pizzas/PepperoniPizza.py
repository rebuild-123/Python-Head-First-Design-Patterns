from Pizza import Pizza


class PepperoniPizza(Pizza):
    def __init__(self):
        self.name = "Pepperoni Pizza"
        self.dough = "Crust"
        self.sauce = "Marinara sauce"
        self.toppings = [] # Avoid sharing "toppings" with subclass of class "Pizza".
        self.toppings.append("Sliced Pepperoni")
        self.toppings.append("Sliced Onion")
        self.toppings.append("Grated parmesan cheese")