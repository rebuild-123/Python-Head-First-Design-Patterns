from Accommodation import Accommodation


class Tent(Accommodation):
    siteNumber: int = 0
    def __init__(self, name: str = "Tent"):
        self.name = name
    def setSiteNumber(self, n: int) -> None:
        self.siteNumber = n
    def getSiteNumber(self) -> int:
        return self.siteNumber
    def getLocation(self) -> str:
        if self.siteNumber == 0: return ""
        else: return f'Site number {self.siteNumber}'