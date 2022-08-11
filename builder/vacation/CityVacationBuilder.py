from Hotel import Hotel
from Reservation import Reservation
from VacationBuilder import VacationBuilder


class CityVacationBuilder(VacationBuilder):
    def __init__(self):
        self.name = "City Vacation Builder"
        self.accommodations = []
        self.events = []
    def addAccommodation_1(self) -> VacationBuilder:
        self.accommodations.append(str(Hotel()))
        return self
    def addAccommodation_2(self, name) -> VacationBuilder:
        self.accommodations.append(str(Hotel(name)))
        return self
    def addAccommodation_3(self, name: str, year: int, month: int, day: int, nights: int, location: int) -> VacationBuilder:
        reservation: Reservation = Reservation()
        reservation.setArrivalDate(year, month, day)
        reservation.setNights(nights)
        
        hotel: Hotel = Hotel(name)
        hotel.setReservation(reservation)
        hotel.setRoomNumber(location)
        self.accommodations.append(str(hotel))
        return self
    def addEvent(self, event: str) -> VacationBuilder:
        self.events.append(f"See the {event} show")
        return self