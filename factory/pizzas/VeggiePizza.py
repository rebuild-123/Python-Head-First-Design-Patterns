from Pizza import Pizza


class VeggiePizza(Pizza):
    def __init__(self):
        self.name = "Veggie Pizza"
        self.dough = "Crust"
        self.sauce = "Marinara sauce"
        self.toppings = [] # Avoid sharing "toppings" with subclass of class "Pizza".
        self.toppings.append("Shredded mozzarella")
        self.toppings.append("Grated parmesan")
        self.toppings.append("Diced onion")
        self.toppings.append("Sliced mushrooms")
        self.toppings.append("Sliced red pepper")
        self.toppings.append("Sliced black olives")