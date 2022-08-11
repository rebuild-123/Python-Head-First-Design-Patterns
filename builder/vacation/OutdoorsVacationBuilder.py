from Reservation import Reservation
from Tent import Tent
from VacationBuilder import VacationBuilder


class OutdoorsVacationBuilder(VacationBuilder):
    def __init__(self):
        self.name = "Outdoorsy Vacation Builder"
        self.accommodations = []
        self.events = []
    def addAccommodation_1(self) -> VacationBuilder:
        self.accommodations.append(str(Tentl()))
        return self
    def addAccommodation_2(self, name) -> VacationBuilder:
        self.accommodations.append(str(Tent(name)))
        return self
    def addAccommodation_3(self, name: str, year: int, month: int, day: int, nights: int, location: int) -> VacationBuilder:
        reservation: Reservation = Reservation()
        reservation.setArrivalDate(year, month, day)
        reservation.setNights(nights)
        
        tent: Tent = Tent(name)
        tent.setReservation(reservation)
        tent.setSiteNumber(location)
        self.accommodations.append(str(tent))
        return self
    def addEvent(self, event: str) -> VacationBuilder:
        self.events.append(f"Hike: {event}")
        return self