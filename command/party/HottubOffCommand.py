from Command import Command
from Hottub import Hottub


class HottubOffCommand(Command):
    hottub: Hottub
        
    def __init__(self, hottub: Hottub):
        self.hottub = hottub
        
    def execute(self) -> None:
        self.hottub.setTemperature(98)
        self.hottub.off()
        
    def undo(self) -> None:
        self.hottub.on()