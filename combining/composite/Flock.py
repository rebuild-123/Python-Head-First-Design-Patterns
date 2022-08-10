from typing import Iterator, List

from Quackable import Quackable


class Flock(Quackable):
    quackers: List[Quackable]
        
    def __init__(self):
        self.quackers = []
        
    def add(self, quacker: Quackable):
        self.quackers.append(quacker)
        
    def quack(self) -> None:
        iterator: Iterator[Quackable] = iter(self.quackers)
        quacker: Quackable = next(iterator, None)
        while quacker != None:
            quacker.quack()
            quacker: Quackable = next(iterator, None)
                
    # toString
    def __str__(self) -> str:
        return "Flock of Quackers"
    
    # toString for print
    def __repr__(self) -> str:
        return str(self)