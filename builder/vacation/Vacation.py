from typing import List

class StringBuffer:
    def __init__(self) -> None:
        self.ls: List[str] = []

    def append(self, string: str) -> None:
        self.ls.append(string)

    def toString(self) -> str:
        return "".join(self.ls)


class Vacation:
    name: str
    accommodations: List[str]
    events: List[str]

    def __init__(self) -> None:
        self.accommodations: List[str] = []
        self.events: List[str] = []

    def setName(self, name: str) -> None:
        self.name = name

    def setAccommodations(self, accommodations: List[str]) -> None:
        self.accommodations = accommodations

    def setEvents(self, events: List[str]) -> None:
        self.events = events

    # toString
    def __str__(self) -> str:
        display: StringBuffer = StringBuffer()
        display.append(f"---- {self.name} ----\n")
        for a in self.accommodations:
            display.append(a)
        for e in self.events:
            display.append(f"{e}\n")
        return display.toString()

    # toString for print
    def __repr__(self) -> str:
        return str(self)
