from Observer import Observer
from QuackObservable import QuackObservable


class Quackologist(Observer):
    
    def update(self, duck: QuackObservable) -> None:
        print(f"Quackologist: {duck} just quacked.")
        
    # toString
    def __str__(self) -> str:
        return "Quackologist"
    
    # toString for print
    def __repr__(self) -> str:
        return str(self)