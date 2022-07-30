from abc import ABC, abstractmethod

from Pizza import Pizza


class PizzaStore(ABC):
    @abstractmethod
    def _createPizza(self, item: str) -> Pizza:
        raise NotImplementedError
        
    def orderPizza(self, type_: str) -> Pizza:
        pizza: Pizza = self._createPizza(type_)
        print(f"--- Making a {pizza.getName()} ---")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza