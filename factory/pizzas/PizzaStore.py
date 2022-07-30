from Pizza import Pizza
from SimplePizzaFactory import SimplePizzaFactory


class PizzaStore:
    factory: SimplePizzaFactory
    
    def __init__(self, factory: SimplePizzaFactory):
        self.factory = factory
        
    def orderPizza(self, type_: str) -> Pizza:
        pizza: Pizza
            
        pizza = self.factory.createPizza(type_)
        
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        
        return pizza