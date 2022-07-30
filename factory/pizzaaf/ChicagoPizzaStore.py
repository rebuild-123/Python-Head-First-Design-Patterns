from CheesePizza import CheesePizza
from ChicagoPizzaIngredientFactory import ChicagoPizzaIngredientFactory
from ClamPizza import ClamPizza
from PepperoniPizza import PepperoniPizza
from Pizza import Pizza
from PizzaIngredientFactory import PizzaIngredientFactory
from PizzaStore import PizzaStore
from VeggiePizza import VeggiePizza


class ChicagoPizzaStore(PizzaStore):
    def _createPizza(self, item: str) -> Pizza:
        pizza: Pizza = None
        ingredientFactory = PizzaIngredientFactory = ChicagoPizzaIngredientFactory()
        
        if item == "cheese":
            
            pizza = CheesePizza(ingredientFactory)
            pizza.setName("Chicago Style Cheese Pizza")
            
        elif item == "veggie":
            
            pizza = VeggiePizza(ingredientFactory)
            pizza.setName("Chicago Style Veggie Pizza")
            
        elif item == "clam":
            
            pizza = ClamPizza(ingredientFactory)
            pizza.setName("Chicago Style Clam Pizza")
            
        elif item == "pepperoni":
            
            pizza = PepperoniPizza(ingredientFactory)
            pizza.setName("Chicago Style Pepperoni Pizza")
            
        return pizza