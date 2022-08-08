from typing import Iterator

from MenuComponent import MenuComponent


class NullIterator(Iterator[MenuComponent]):
    
    # next
    def __next__(self) -> MenuComponent:
        raise StopIteration
    
    def hasNext(self) -> bool:
        return False