from datetime import datetime


class Tree:
    def display(self, x: int, y: int) -> None:
        pass
    def isWithinRange(self, aDate: datetime) -> bool:
        month = aDate.month
        return (month > 2) and (month < 11)