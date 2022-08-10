from Goose import Goose
from Quackable import Quackable


class GooseAdapter(Quackable):
    goose: Goose
        
    def __init__(self, goose: Goose):
        self.goose = goose
        
    def quack(self) -> None:
        self.goose.honk()
        
    # toString
    def __str__(self) -> str:
        return "Goose pretending to be a Duck"
    
    # toString for print
    def __repr__(self) -> str:
        return str(self)