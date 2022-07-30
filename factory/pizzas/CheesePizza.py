from Pizza import Pizza


class CheesePizza(Pizza):
    def __init__(self):
        self.name = "Cheese Pizza"
        self.dough = "Regular Crust"
        self.sauce = "Marinara Pizza Sauce"
        self.toppings = [] # Avoid sharing "toppings" with subclass of class "Pizza".
        self.toppings.append("Fresh Mozzarella")
        self.toppings.append("Parmesan")