from typing import List

from Calendar import Calendar
from ZoneFactory import ZoneFactory


class PacificCalendar(Calendar):
    def __init__(self, zoneFactory: ZoneFactory):
        self.zone = zoneFactory.createZone("US/Pacific")
        
    def createCalendar(self, appointments: List[str]) -> None:
        # make calendar from appointments
        print("Making the calendar")