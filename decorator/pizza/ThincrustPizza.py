from Pizza import Pizza


class ThincrustPizza(Pizza):
    def __init__(self):
        self.description = "Thin crust pizza, with tomato sauce"
    
    def cost(self) -> float:
        return 7.99