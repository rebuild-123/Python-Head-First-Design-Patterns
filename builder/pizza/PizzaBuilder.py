from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

from Pizza import Pizza


class PizzaBuilder(ABC):
    name: str
    toppings: List[str]
        
    @abstractmethod
    def addCheese(self) -> PizzaBuilder:
        pass
    @abstractmethod
    def addSauce(self) -> PizzaBuilder:
        pass
    @abstractmethod
    def addTomatoes(self) -> PizzaBuilder:
        pass
    @abstractmethod
    def addGarlic(self) -> PizzaBuilder:
        pass
    @abstractmethod
    def addOlives(self) -> PizzaBuilder:
        pass
    @abstractmethod
    def addSpinach(self) -> PizzaBuilder:
        pass
    @abstractmethod
    def addPepperoni(self) -> PizzaBuilder:
        pass
    @abstractmethod
    def addSausage(self) -> PizzaBuilder:
        pass
    def build(self) -> Pizza:
        pizza: Pizza = Pizza()
        pizza.setName(self.name)
        pizza.addToppings(self.toppings)
        return pizza