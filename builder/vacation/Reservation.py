from datetime import datetime


class Reservation:
    arrivalDate: datetime
    nights: int
        
    def setArrivalDate(self, year: int, month: int, day: int) -> None:
        self.arrivalDate = datetime.strptime(f'{year}, {month}, {day}', '%Y, %m, %d')
    def getArrivalDate(self) -> datetime:
        return self.arrivalDate
    def setNights(self, nights: int) -> None:
        self.nights = nights
    def getNights(self) -> int:
        return self.nights