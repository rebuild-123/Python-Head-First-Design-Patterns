from CeilingFan import CeilingFan
from Command import Command


class CeilingFanOnCommand(Command):
    ceilingFan: CeilingFan
    
    def __init__(self, ceilingFan: CeilingFan):
        self.ceilingFan = ceilingFan
        
    def execute(self) -> None:
        self.ceilingFan.high()