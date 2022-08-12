from typing import List

from Tree import Tree
from TreeFactory import TreeFactory


class Client:
    @staticmethod
    def main(*args) -> None:
        deciduousLocations: List[List[int]] = [[1, 1], [33, 50], [100, 90]]
        coniferLocations: List[List[int]] = [[10, 87], [24, 76], [2,64]]
        treeFactory: TreeFactory = TreeFactory() # creates the two flyweights
        d: Tree
        c: Tree
        try:
            d = treeFactory.getTree("deciduous")
            c = treeFactory.getTree("conifer")
            for location in deciduousLocations:
                d.display(location[0], location[1])
            for location in coniferLocations:
                c.display(location[0], location[1])
        except Exception as e:
            print(e)
            
if __name__ == "__main__":
    Client.main()