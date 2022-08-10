from typing import List

from EnumerationIterator import Enumeration
from IteratorEnumeration import Iterator


class EI:
    @staticmethod
    def main(args: List[str]) -> None:
        v = args
        print("Using enumeration with Vector")
        enumeration: Enumeration = Enumeration(v)
        while enumeration.hasMoreElements():
            print(enumeration.nextElement())
        print("Using iterator with Vector")
        iterator: Iterator = Iterator(v)
        while iterator.hasNext():
            print(iterator.next())
        print("Using for/in with array of Strings")
        for color in args:
            print(color)
            
if __name__ == "__main__":
    EI.main(['a', 'b', 'c'])