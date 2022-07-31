from Command import Command
from Hottub import Hottub


class HottubOnCommand(Command):
    hottub: Hottub
        
    def __init__(self, hottub: Hottub):
        self.hottub = hottub
        
    def execute(self) -> None:
        self.hottub.on()
        self.hottub.heat()
        self.hottub.bubblesOn()