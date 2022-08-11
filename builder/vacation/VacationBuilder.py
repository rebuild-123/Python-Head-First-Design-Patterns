from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

from Accommodation import Accommodation
from Vacation import Vacation


class VacationBuilder(ABC):
    name: str
    accommodations: List[Accommodation]
    events: List[str]
        
    @abstractmethod
    def addAccommodation_1(self) -> VacationBuilder:
        raise NotImplementedError
    @abstractmethod
    def addAccommodation_2(self, name: str) -> VacationBuilder:
        raise NotImplementedError
    @abstractmethod
    def addAccommodation_3(self, name: str, year: int, month: int, day: int, nights: int, location: int) -> VacationBuilder:
        raise NotImplementedError
    @abstractmethod
    def addEvent(self, event: str) -> VacationBuilder:
        raise NotImplementedError
        
    def getVacation(self) -> Vacation:
        vacation: Vacation = Vacation()
        vacation.setName(self.name)
        vacation.setAccommodations(self.accommodations)
        vacation.setEvents(self.events)
        return vacation