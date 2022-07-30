from typing import List

from BlackOlives import BlackOlives
from Cheese import Cheese
from Clams import Clams
from Dough import Dough
from Eggplant import Eggplant
from FrozenClams import FrozenClams
from MozzarellaCheese import MozzarellaCheese
from Pepperoni import Pepperoni
from PizzaIngredientFactory import PizzaIngredientFactory
from PlumTomatoSauce import PlumTomatoSauce
from Sauce import Sauce
from SlicedPepperoni import SlicedPepperoni
from Spinach import Spinach
from ThickCrustDough import ThickCrustDough
from Veggies import Veggies


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def createDough(self) -> Dough:
        return ThickCrustDough()
    
    def createSauce(self) -> Sauce:
        return PlumTomatoSauce()
    
    def createCheese(self) -> Cheese:
        return MozzarellaCheese()
    
    def createVeggies(self) -> List[Veggies]:
        veggies: List[Veggies] = [BlackOlives(), Spinach(), Eggplant()]
        return veggies
    
    def createPepperoni(self) -> Pepperoni:
        return SlicedPepperoni()
    
    def createClam(self) -> Clams:
        return FrozenClams()
    