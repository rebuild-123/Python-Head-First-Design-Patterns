from copy import deepcopy

from Monster import Monster, CloneNotSupportedException


class Dragon(Monster):
    def __init__(self, name: str, hasWings: bool):
        self.name = name
        self.hasWings = hasWings
        self.canBreatheFire = True
    # Each concrete monster could determine how best to clone itself
    def copy(self) -> Monster:
        try:
            return deepcopy(self)
        except:
            raise CloneNotSupportedException