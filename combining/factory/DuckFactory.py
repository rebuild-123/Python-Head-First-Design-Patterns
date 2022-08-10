from AbstractDuckFactory import AbstractDuckFactory
from DuckCall import DuckCall
from MallardDuck import MallardDuck
from Quackable import Quackable
from RedheadDuck import RedheadDuck
from RubberDuck import RubberDuck


class DuckFactory(AbstractDuckFactory):
    
    def createMallardDuck(self) -> Quackable:
        return MallardDuck()
    
    def createRedheadDuck(self) -> Quackable:
        return RedheadDuck()
    
    def createDuckCall(self) -> Quackable:
        return DuckCall()
    
    def createRubberDuck(self) -> Quackable:
        return RubberDuck()