from Quackable import Quackable


class MallardDuck(Quackable):
    def quack(self) -> None:
        print("Quack")
        
    # toString
    def __str__(self) -> str:
        return "Mallard Duck"
    
    # toString for print
    def __repr__(self) -> str:
        return str(self)