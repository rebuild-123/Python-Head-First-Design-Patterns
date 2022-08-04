from typing import List

from IteratorEnumeration import Enumeration, Iterator, IteratorEnumeration


class IteratorEnumerationTestDrive:
    @staticmethod
    def main(args: List[str]) -> None:
        l = Iterator(args)
        enumeration: Enumeration = IteratorEnumeration(l)
        while enumeration.hasMoreElements():
            print(enumeration.nextElement())