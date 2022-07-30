from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float) -> None:
        raise NotImplementedError