from __future__ import annotations
from abc import ABC, abstractmethod


class CloneNotSupportedException(Exception): pass

class StringBuffer:
    def __init__(self):
        self.ls = []
        
    def append(self, string: str) -> None:
        self.ls.append(string)
        
    def toString(self) -> str:
        return ''.join(self.ls)

class Monster:
    eatsChildren: bool = True
    hasWings: bool = False
    numHeads: int = 1
    canBreatheFire: bool = False
    name: str
    def __init__(self, name: str):
        self.name = name
    def spitPoison(self) -> None: # default is do nothing
        pass
    def setName(self, name: str) -> None:
        self.name = name
    @abstractmethod
    def copy(self) -> Monster:
        raise CloneNotSupportedException
        
    # toString
    def __str__(self) -> str:
        s: StringBuffer = StringBuffer()
        s.append(f"I'm a monster named {self.name} with {self.numHeads} head(s). ")
        if self.canBreatheFire: s.append("I can breathe fire. ")
        if self.eatsChildren: s.append("I eat children. ")
        if self.hasWings: s.append("I have wings. ")
        return s.toString()
    
    # toString for print
    def __repr__(self) -> str:
        return str(self)