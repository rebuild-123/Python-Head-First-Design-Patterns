from RemoteControl import RemoteControl
from TVFactory import TVFactory


class SpecialRemote(RemoteControl):
    def __init__(self, tvFactory: TVFactory):
        super().__init__(tvFactory)
    def up(self) -> None:
        channel: int = self.getChannel()
        self.setChannel(channel+1)
    def down(self) -> None:
        channel: int = self.getChannel()
        self.setChannel(channel-1)