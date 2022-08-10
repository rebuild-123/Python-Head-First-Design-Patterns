from AbstractDuckFactory import AbstractDuckFactory
from DuckCall import DuckCall
from MallardDuck import MallardDuck
from Quackable import Quackable
from QuackCounter import QuackCounter
from RedheadDuck import RedheadDuck
from RubberDuck import RubberDuck


class CountingDuckFactory(AbstractDuckFactory):
    
    def createMallardDuck(self) -> Quackable:
        return QuackCounter(MallardDuck())
    
    def createRedheadDuck(self) -> Quackable:
        return QuackCounter(RedheadDuck())
    
    def createDuckCall(self) -> Quackable:
        return QuackCounter(DuckCall())
    
    def createRubberDuck(self) -> Quackable:
        return QuackCounter(RubberDuck())