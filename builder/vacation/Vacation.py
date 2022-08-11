from typing import List

from Accommodation import Accommodation


class StringBuffer:
    def __init__(self):
        self.ls = []
        
    def append(self, string: str) -> None:
        self.ls.append(string)
        
    def toString(self) -> str:
        return ''.join(self.ls)

class Vacation:
    name: str
    accommodations: List[Accommodation]
    events: List[str]
        
    def __init__(self):
        self.accommodations = []
        self.events = []
        
    def setName(self, name: str) -> None:
        self.name = name
        
    def setAccommodations(self, accommodations: List[Accommodation]) -> None:
        self.accommodations = accommodations
        
    def setEvents(self, events: List[str]) -> None:
        self.events = events
        
    # toString
    def __str__(self) -> str:
        display: StringBuffer = StringBuffer()
        display.append(f"---- {self.name} ----\n")
        for a in self.accommodations:
            display.append(a)
        for e in self.events:
            display.append(f'{e}\n')
        return display.toString()
    
    # toString for print
    def __repr__(self) -> str:
        return str(self)