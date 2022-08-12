from copy import deepcopy

from Monster import Monster, CloneNotSupportedException


class Drakon(Monster):
    def __init__(self, name: str, numHeads: int, canBreatheFire: bool):
        self.name = name
        self.numHeads = numHeads
        self.canBreatheFire = canBreatheFire
    def spitPoison(self) -> None:
        print(f'{self.name} spits poison')
    # Each concrete monster could determine how best to clone itself
    def copy(self) -> Monster:
        try:
            return deepcopy(self)
        except:
            raise CloneNotSupportedException