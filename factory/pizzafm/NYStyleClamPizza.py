from Pizza import Pizza


class NYStyleClamPizza(Pizza):
    def __init__(self):
        self.name = "NY Style Clam Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings = [] # Avoid sharing "toppings" with subclass of class "Pizza".
        self.toppings.append("Grated Reggiano Cheese")
        self.toppings.append("Fresh Clams from Long Island Sound")