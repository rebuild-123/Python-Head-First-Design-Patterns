from typing import List

from Cheese import Cheese
from Clams import Clams
from Dough import Dough
from Pepperoni import Pepperoni
from Sauce import Sauce
from Veggies import Veggies


class PizzaIngredientFactory:
    def createDough(self) -> Dough:
        pass
    def createSauce(self) -> Sauce:
        pass
    def createCheese(self) -> Cheese:
        pass
    def createVeggies(self) -> List[Veggies]:
        pass
    def createPepperoni(self) -> Pepperoni:
        pass
    def createClam(self) -> Clams:
        pass