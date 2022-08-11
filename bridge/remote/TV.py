from abc import ABC, abstractmethod


class TV(ABC):
    @abstractmethod
    def on(self) -> None:
        pass
    @abstractmethod
    def off(self) -> None:
        pass
    @abstractmethod
    def tuneChannel(self, channel: int) -> None:
        pass
    @abstractmethod
    def getChannel(self) -> int:
        pass