from Pizza import Pizza


class NYStylePepperoniPizza(Pizza):
    def __init__(self):
        self.name = "NY Style Pepperoni Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings = [] # Avoid sharing "toppings" with subclass of class "Pizza".
        self.toppings.append("Grated Reggiano Cheese")
        self.toppings.append("Sliced Pepperoni")
        self.toppings.append("Garlic")
        self.toppings.append("Onion")
        self.toppings.append("Mushrooms")
        self.toppings.append("Red Pepper")