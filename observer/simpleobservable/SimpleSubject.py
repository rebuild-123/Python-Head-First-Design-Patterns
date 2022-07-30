from Observable import Observable
from Observer import Observer


class SimpleSubject(Observable):
    __value: int = 0
    
    def __init__(self):
        super().__init__()
    
    def setValue(self, value: int) -> None:
        self.__value = value
        self.setChanged()
        self.notifyObservers(value)
        
    def getValue(self) -> int:
        return self.__value