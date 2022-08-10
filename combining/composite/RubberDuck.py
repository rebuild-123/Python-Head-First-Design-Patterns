from Quackable import Quackable


class RubberDuck(Quackable):
    def quack(self) -> None:
        print("Squeak")
        
    # toString
    def __str__(self) -> str:
        return "Rubber Duck"
    
    # toString for print
    def __repr__(self) -> str:
        return str(self)