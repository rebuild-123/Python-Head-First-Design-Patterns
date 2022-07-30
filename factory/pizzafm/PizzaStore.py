from abc import ABC, abstractmethod
from Pizza import Pizza


class PizzaStore(ABC):
    
    @abstractmethod
    def createPizza(self, item: str) -> Pizza:
        raise NotImplementedError
        
    def orderPizza(self, type_: str) -> Pizza:
        pizza: Pizza = self.createPizza(type_)
        print(f'--- Making a {pizza.getName()} ---')
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza