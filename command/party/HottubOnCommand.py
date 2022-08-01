from Command import Command
from Hottub import Hottub


class HottubOnCommand(Command):
    hottub: Hottub
        
    def __init__(self, hottub: Hottub):
        self.hottub = hottub
        
    def execute(self) -> None:
        self.hottub.on()
        self.hottub.setTemperature(104)
        self.hottub.circulate()
        
    def undo(self) -> None:
        self.hottub.off()