from typing import List

from EnumerationIterator import Enumeration, EnumerationIterator, Iterator


class EnumerationIteratorTestDrive:
    @staticmethod
    def main(args: List[str]) -> None:
        v = Enumeration(args)
        iterator: Iterator = EnumerationIterator(v)
        while iterator.hasNext():
            print(iterator.next())