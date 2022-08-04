from typing import List

from EnumerationIterator import Enumeration
from IteratorEnumeration import Iterator


class EI:
    @staticmethod
    def main(args: List[str]) -> None:
        v = args
        enumeration: Enumeration = Enumeration(v)
        while enumeration.hasMoreElements():
            print(enumeration.nextElement())
        iterator: Iterator = Iterator(v)
        while iterator.hasNext():
            print(iterator.next())
            
if __name__ == "__main__":
    EI.main(['a', 'b', 'c'])