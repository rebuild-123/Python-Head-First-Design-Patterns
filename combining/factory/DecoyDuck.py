from Quackable import Quackable


class DecoyDuck(Quackable):
    def quack(self) -> None:
        print("<< Silence >>")
        
    # toString
    def __str__(self) -> str:
        return "Decoy Duck"
    
    # toString for print
    def __repr__(self) -> str:
        return str(self)