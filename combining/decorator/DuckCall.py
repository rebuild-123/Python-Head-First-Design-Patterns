from Quackable import Quackable


class DuckCall(Quackable):
    def quack(self) -> None:
        print("Kwak")
        
    # toString
    def __str__(self) -> str:
        return "Duck Call"
    
    # toString for print
    def __repr__(self) -> str:
        return str(self)