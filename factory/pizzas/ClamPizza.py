from Pizza import Pizza


class ClamPizza(Pizza):
    def __init__(self):
        self.name = "Clam Pizza"
        self.dough = "Thin crust"
        self.sauce = "White garlic sauce"
        self.toppings = [] # Avoid sharing "toppings" with subclass of class "Pizza".
        self.toppings.append("Clams")
        self.toppings.append("Grated parmesan cheese")