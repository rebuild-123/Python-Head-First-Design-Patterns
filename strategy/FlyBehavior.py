from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self) -> None:
        raise NotImplementedError