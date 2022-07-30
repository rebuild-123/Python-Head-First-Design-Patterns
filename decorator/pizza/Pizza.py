from abc import ABC, abstractmethod


class Pizza(ABC):
    description: str = "Basic Pizza"
        
    def getDescription(self) -> str:
        return self.description
    
    @abstractmethod
    def cost(self) -> float:
        raise NotImplementedError