from abc import ABC, abstractmethod
from enum import Enum

from Size import Size


class Beverage(ABC):
    Size: Enum = Size
    size = Size.TALL
    description: str = "Unknown Beverage"
        
    def getDescription(self) -> str:
        return self.description
    
    def setSize(self, size: Size) -> None:
        self.size = size
    
    def getSize(self) -> Size:
        return self.size
    
    @abstractmethod
    def cost(self) -> float:
        raise NotImplementedError