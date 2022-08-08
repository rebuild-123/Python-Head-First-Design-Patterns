from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterator


class UnsupportedOperationException(Exception): pass

class MenuComponent(ABC):
    
    def add(self, menuComponent: MenuComponent) -> None:
        raise UnsupportedOperationException
    def remove(self, menuComponent: MenuComponent) -> None:
        raise UnsupportedOperationException
    def getChild(self, i: int) -> MenuComponent:
        raise UnsupportedOperationException
        
    def getName(self) -> str:
        raise UnsupportedOperationException
    def getDescription(self) -> str:
        raise UnsupportedOperationException
    def getPrice(self) -> float:
        raise UnsupportedOperationException
    def isVegetarian(self) -> bool:
        raise UnsupportedOperationException
        
    def print(self) -> None:
        raise UnsupportedOperationException