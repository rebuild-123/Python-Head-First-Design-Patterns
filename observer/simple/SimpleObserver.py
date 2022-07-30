from Observer import Observer
from SimpleSubject import SimpleSubject
from Subject import Subject


class SimpleObserver(Observer):
    __value: int
    __simpleSubject: Subject
    
    def __init__(self, simpleSubject: Subject):
        self.__simpleSubject = simpleSubject
        self.__simpleSubject.registerObserver(self)
        
    def update(self, value: int) -> None:
        self.__value = value
        self.display()
        
    def display(self) -> None:
        print(f'Value: {self.__value}')