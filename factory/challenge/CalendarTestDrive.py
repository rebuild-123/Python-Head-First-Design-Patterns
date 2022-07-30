from typing import List

from Calendar import Calendar
from PacificCalendar import PacificCalendar
from ZoneFactory import ZoneFactory


class CalendarTestDrive:
    @staticmethod
    def main(*args) -> None:
        zoneFactory: ZoneFactory = ZoneFactory()
        calendar: Calendar = PacificCalendar(zoneFactory)
        appts: List[str] = ["appt 1", "appt 2"]
        calendar.createCalendar(appts)
        calendar.print_()
        
if __name__ == "__main__":
    CalendarTestDrive.main()