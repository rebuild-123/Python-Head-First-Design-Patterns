from datetime import datetime

from Tree import Tree


class DeciduousTree(Tree):
    # complex trunk, branch, leaf graphic data
    def display(self, x: int, y: int) -> None:
        print(f"Deciduous tree is located at {x}, {y}")
        if not self.isWithinRange(aDate=datetime.now()):
            print("The tree currently has no leaves")