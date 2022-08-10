from abc import ABC, abstractmethod

from Quackable import Quackable


class AbstractDuckFactory(ABC):
    
    @abstractmethod
    def createMallardDuck(self) -> Quackable:
        raise NotImplementedError
    @abstractmethod
    def createRedheadDuck(self) -> Quackable:
        raise NotImplementedError
    @abstractmethod
    def createDuckCall(self) -> Quackable:
        raise NotImplementedError
    @abstractmethod
    def createRubberDuck(self) -> Quackable:
        raise NotImplementedError