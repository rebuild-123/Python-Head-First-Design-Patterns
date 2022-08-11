from RemoteControl import RemoteControl
from TVFactory import TVFactory


class GenericRemote(RemoteControl):
    def __init__(self, tvFactory: TVFactory):
        super().__init__(tvFactory)
    def nextChannel(self) -> None:
        channel: int = self.getChannel()
        self.setChannel(channel+1)
    def prevChannel(self) -> None:
        channel: int = self.getChannel()
        self.setChannel(channel-1)