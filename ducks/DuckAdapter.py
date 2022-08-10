from random import randint

from Duck import Duck
from Turkey import Turkey


class DuckAdapter(Turkey):
    duck: Duck
    rand: randint
        
    def __init__(self, duck: Duck):
        self.duck = duck
        self.rand = randint
        
    def gobble(self) -> None:
        self.duck.quack()
        
    def fly(self) -> None:
        if self.rand(0,5) == 0:
            self.duck.fly()