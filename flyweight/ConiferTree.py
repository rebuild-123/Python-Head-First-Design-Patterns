from datetime import datetime

from Tree import Tree


class ConiferTree(Tree):
    # Complex trunk, branch, needle graphic data
    def display(self, x: int, y: int) -> None:
        print(f"Conifer tree is located at {x}, {y}")