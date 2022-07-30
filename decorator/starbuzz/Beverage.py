from abc import ABC, abstractmethod


class Beverage(ABC):
    description: str = "Unknown Beverage"
        
    def getDescription(self) -> str:
        return self.description
    
    @abstractmethod
    def cost(self) -> float:
        raise NotImplementedError