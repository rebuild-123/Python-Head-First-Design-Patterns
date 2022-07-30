from CheesePizza import CheesePizza
from ClamPizza import ClamPizza
from NYPizzaIngredientFactory import NYPizzaIngredientFactory
from PepperoniPizza import PepperoniPizza
from Pizza import Pizza
from PizzaIngredientFactory import PizzaIngredientFactory
from PizzaStore import PizzaStore
from VeggiePizza import VeggiePizza


class NYPizzaStore(PizzaStore):
    def _createPizza(self, item: str) -> Pizza:
        pizza: Pizza = None
        ingredientFactory = PizzaIngredientFactory = NYPizzaIngredientFactory()
        
        if item == "cheese":
            
            pizza = CheesePizza(ingredientFactory)
            pizza.setName("New York Style Cheese Pizza")
            
        elif item == "veggie":
            
            pizza = VeggiePizza(ingredientFactory)
            pizza.setName("New York Style Veggie Pizza")
            
        elif item == "clam":
            
            pizza = ClamPizza(ingredientFactory)
            pizza.setName("New York Style Clam Pizza")
            
        elif item == "pepperoni":
            
            pizza = PepperoniPizza(ingredientFactory)
            pizza.setName("New York Style Pepperoni Pizza")
            
        return pizza