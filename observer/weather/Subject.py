from abc import ABC, abstractmethod

from Observer import Observer

class Subject(ABC):
    @abstractmethod
    def registerObserver(self, o: Observer) -> None:
        raise NotImplementedError
        
    @abstractmethod
    def removeObserver(self, o: Observer) -> None:
        raise NotImplementedError
        
    @abstractmethod
    def notifyObservers(self) -> None:
        raise NotImplementedError