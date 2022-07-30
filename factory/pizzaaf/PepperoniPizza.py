from Pizza import Pizza
from PizzaIngredientFactory import PizzaIngredientFactory


class PepperoniPizza(Pizza):
    ingredientFactory: PizzaIngredientFactory
        
    def __init__(self, ingredientFactory: PizzaIngredientFactory):
        self.ingredientFactory = ingredientFactory
        self.veggies = [] # Avoid sharing "veggies" with subclass of class "Pizza".
        
    def prepare(self) -> None:
        print(f'Preparing {self.name}')
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        self.veggies = self.ingredientFactory.createVeggies()
        self.pepperoni = self.ingredientFactory.createPepperoni()