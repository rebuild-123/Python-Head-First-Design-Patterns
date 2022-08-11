from Accommodation import Accommodation


class Hotel(Accommodation):
    roomNumber: int = 0
    def __init__(self, name: str = "Hotel"):
        self.name = name
    def setRoomNumber(self, n: int) -> None:
        self.roomNumber = n
    def getRoomNumber(self) -> int:
        return self.roomNumber
    def getLocation(self) -> str:
        if self.roomNumber == 0: return ""
        else: return f'Room number {self.roomNumber}'