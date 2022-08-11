from abc import ABC, abstractmethod

from Reservation import Reservation


class StringBuffer:
    def __init__(self):
        self.ls = []
        
    def append(self, string: str) -> None:
        self.ls.append(string)
        
    def toString(self) -> str:
        return ''.join(self.ls)

class Accommodation(ABC):
    name: str
    reservation: Reservation = None
        
    def setReservation(self, r: Reservation) -> None:
        self.reservation = r
    def getReservation(self) -> Reservation:
        return self.reservation
    @abstractmethod
    def getLocation(self) -> str:
        pass
    
    # toString
    def __str__(self) -> str:
        display: StringBuffer = StringBuffer()
        display.append(f"You're staying at {self.name}")
        if self.reservation != None:
            display.append(f"\nYou have a reservation for arrival date: {self.reservation.getArrivalDate()}, staying for {self.reservation.getNights()} nights")
        if self.getLocation() != "":
            display.append(f" in {self.getLocation()}")
        display.append("\n")
        return display.toString()
    
    #toString for print
    def __repr__(self) -> str:
        return str(self)