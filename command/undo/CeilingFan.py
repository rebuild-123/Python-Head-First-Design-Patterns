from typing import Final


class CeilingFan:
    HIGH: Final[int] = 3
    MEDIUM: Final[int] = 2
    LOW: Final[int] = 1
    OFF: Final[int] = 0
    location: str = ""
    speed: int = 0
        
    def __init__(self, location: str):
        self.location = location
        self.speed = self.OFF
        
    def high(self) -> None:
        # turns the ceiling fan on to high
        self.speed = self.HIGH
        print(f'{self.location} ceiling fan is on high')
        
    def medium(self) -> None:
        # turns the ceiling fan on to medium
        self.speed = self.MEDIUM
        print(f'{self.location} ceiling fan is on medium')
        
    def low(self) -> None:
        # turns the ceiling fan on to low
        self.speed = self.LOW
        print(f'{self.location} ceiling fan is on low')
        
    def off(self) -> None:
        # turns the ceiling fan off
        self.speed = self.OFF
        print(f'{self.location} ceiling fan is off')
        
    def getSpeed(self) -> int:
        return self.speed