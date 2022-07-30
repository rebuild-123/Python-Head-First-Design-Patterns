from abc import ABC, abstractmethod
from typing import List

from Zone import Zone


class Calendar(ABC):
    zone: Zone
    
    def print_(self) -> None:
        print(f"--- {self.zone.getDisplayName()} Calendar ---")
        # print all appointments in correct time zone
        print(f"Offset from GMT: {self.zone.getOffset()}")
        
    @abstractmethod
    def createCalendar(self, appointments: List[str]) -> None:
        raise NotImplementedError