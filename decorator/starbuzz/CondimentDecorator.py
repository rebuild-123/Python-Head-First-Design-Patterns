from abc import ABC, abstractmethod

from Beverage import Beverage


class CondimentDecorator(Beverage):
    beverage: Beverage
    
    @abstractmethod
    def getDescription(self) -> str:
        raise NotImplementedError