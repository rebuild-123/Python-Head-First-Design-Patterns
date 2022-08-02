from typing import Final


class CeilingFan:
    location: str = ""
    level: int
    HIGH: Final[int] = 2
    MEDIUM: Final[int] = 1
    LOW: Final[int] = 0
        
    def __init__(self, location: str):
        self.location = location
        
    def high(self) -> None:
        # turns the ceiling fan on to high
        self.level = self.HIGH
        print(f'{self.location} ceiling fan is on high')
        
    def medium(self) -> None:
        # turns the ceiling fan on to medium
        self.level = self.MEDIUM
        print(f'{self.location} ceiling fan is on medium')
        
    def low(self) -> None:
        # turns the ceiling fan on to low
        self.level = self.LOW
        print(f'{self.location} ceiling fan is on low')
        
    def off(self) -> None:
        # turns the ceiling fan off
        self.level = 0
        print(f'{self.location} ceiling fan is off')
        
    def getSpeed(self) -> int:
        return self.level