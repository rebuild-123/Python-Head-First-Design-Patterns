from typing import List

from Cheese import Cheese
from Clams import Clams
from Dough import Dough
from FreshClams import FreshClams
from Garlic import Garlic
from MarinaraSauce import MarinaraSauce
from Mushroom import Mushroom
from Onion import Onion
from Pepperoni import Pepperoni
from PizzaIngredientFactory import PizzaIngredientFactory
from RedPepper import RedPepper
from ReggianoCheese import ReggianoCheese
from Sauce import Sauce
from SlicedPepperoni import SlicedPepperoni
from ThickCrustDough import ThickCrustDough
from Veggies import Veggies


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def createDough(self) -> Dough:
        return ThickCrustDough()
    
    def createSauce(self) -> Sauce:
        return MarinaraSauce()
    
    def createCheese(self) -> Cheese:
        return ReggianoCheese()
    
    def createVeggies(self) -> List[Veggies]:
        veggies: List[Veggies] = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies
    
    def createPepperoni(self) -> Pepperoni:
        return SlicedPepperoni()
    
    def createClam(self) -> Clams:
        return FreshClams()
    