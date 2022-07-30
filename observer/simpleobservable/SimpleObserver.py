from Observable import Observable
from Observer import Observer
from SimpleSubject import SimpleSubject

class SimpleObserver(Observer):
    __value: int
    __observable: Observable
        
    def __init__(self, observable: Observable):
        self.__observable = observable
        self.__observable.addObserver(self)
        
    def display(self) -> None:
        print(f"Value: {self.__value}")
        
    def update(self, o: Observable, arg: object) -> None:
        print(arg)
        self.__value = int(arg)
        self.display()
        if isinstance(o, SimpleSubject):
            simpleSubject: SimpleSubject = o
            self.__value = simpleSubject.getValue()
            self.display()