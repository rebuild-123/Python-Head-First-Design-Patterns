from Command import Command
from TV import TV


class TVOffCommand(Command):
    tv: TV
        
    def __init__(self, tv: TV):
        self.tv = tv
        
    def execute(self) -> None:
        self.tv.off()
        
    def undo(self) -> None:
        self.tv.on()