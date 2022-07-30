from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, value: int) -> None:
        raise NotImplementedError