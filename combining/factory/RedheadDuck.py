from Quackable import Quackable


class RedheadDuck(Quackable):
    def quack(self) -> None:
        print("Quack")
        
    # toString
    def __str__(self) -> str:
        return "Redhead Duck"
    
    # toString for print
    def __repr__(self) -> str:
        return str(self)