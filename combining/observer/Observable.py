from typing import List, Iterator

from Observer import Observer
from QuackObservable import QuackObservable


class Observable(QuackObservable):
    observers: List[Observer] = []
    duck: QuackObservable
        
    def __init__(self, duck: QuackObservable):
        self.duck = duck
        self.observers = []
        
    def registerObserver(self, observer: Observer) -> None:
        self.observers.append(observer)
        
    def notifyObservers(self) -> None:
        iterator: Iterator[Observer] = iter(self.observers)
        observer: Observer = next(iterator, None)
        while observer != None:
            observer.update(self.duck)
            observer: Observer = next(iterator, None)
                
    def getObservers(self) -> Iterator[Observer]:
        return iter(self.observers)