from abc import ABC, abstractmethod

from TV import TV
from TVFactory import TVFactory


class RemoteControl(ABC):
    tv: TV
    tvFactory: TVFactory
    def __init__(self, tvFactory: TVFactory):
        self.tvFactory = tvFactory
    def on(self) -> None:
        self.tv.on()
    def off(self) -> None:
        self.tv.off()
    def setChannel(self, channel: int) -> None:
        self.tv.tuneChannel(channel)
    def getChannel(self) -> int:
        return self.tv.getChannel()
    def setTV(self, type_: str) -> None:
        try:
            self.tv = self.tvFactory.getTV(type_)
        except Exception as e:
            print(e)