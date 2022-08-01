import re
import sys

from CeilingFan import CeilingFan
from Command import Command


class CeilingFanHighCommand(Command):
    ceilingFan: CeilingFan
    prevSpeed: int = 0
    
    def __init__(self, ceilingFan: CeilingFan):
        self.ceilingFan = ceilingFan
        
    def execute(self) -> None:
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.high()
        
    def undo(self) -> None:
        if re.match(r'3\.[1-9][0-9]\.', sys.version[:5]):
            # Only for python 3.10 and later
            match self.prevSpeed:
                case CeilingFan.HIGH: self.ceilingFan.high()
                case CeilingFan.MEDIUM: self.ceilingFan.medium()
                case CeilingFan.LOW: self.ceilingFan.low()
                case _: self.ceilingFan.off()
        else:
            if self.prevSpeed == CeilingFan.HIGH: self.ceilingFan.high()
            elif self.prevSpeed == CeilingFan.MEDIUM: self.ceilingFan.medium()
            elif self.prevSpeed == CeilingFan.LOW: self.ceilingFan.low()
            else: self.ceilingFan.off()