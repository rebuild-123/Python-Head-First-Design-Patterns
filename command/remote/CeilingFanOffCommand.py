from CeilingFan import CeilingFan
from Command import Command


class CeilingFanOffCommand(Command):
    ceilingFan: CeilingFan
    
    def __init__(self, ceilingFan: CeilingFan):
        self.ceilingFan = ceilingFan
        
    def execute(self) -> None:
        self.ceilingFan.off()