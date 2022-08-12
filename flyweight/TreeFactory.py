from ConiferTree import ConiferTree
from DeciduousTree import DeciduousTree
from Tree import Tree


class TreeFactory:
    d: Tree = None
    c: Tree = None
    def __init__(self):
        self.d = DeciduousTree()
        self.c = ConiferTree()
    def getTree(self, type_: str) -> Tree:
        if type_ == "deciduous":
            return self.d
        elif type_ == "conifer":
            return self.c
        else:
            raise Exception("Invalid kind of tree")