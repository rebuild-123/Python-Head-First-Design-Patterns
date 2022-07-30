from Pizza import Pizza


class ThickcrustPizza(Pizza):
    def __init__(self):
        self.description = "Thick crust pizza, with tomato sauce"
    
    def cost(self) -> float:
        return 7.99