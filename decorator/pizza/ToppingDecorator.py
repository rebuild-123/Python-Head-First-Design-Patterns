from abc import abstractmethod

from Pizza import Pizza


class ToppingDecorator(Pizza):
    pizza: Pizza
    
    @abstractmethod
    def getDescription(self) -> str:
        raise NotImplementedError