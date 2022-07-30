from Pizza import Pizza


class NYStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings = [] # Avoid sharing "toppings" with subclass of class "Pizza".
        self.toppings.append("Grated Reggiano Cheese")