from collections import deque
from typing import Deque, Iterator, List

from MenuComponent import MenuComponent


class CompositeIterator(Iterator[MenuComponent]):
    stack: Deque[Iterator[MenuComponent]]
        
    def __init__(self, iterator: Iterator[MenuComponent]):
        self.stack = deque()
        self.stack.append(iterator)
        
    def __iter__(self):
        return self
        
    # next
    def __next__(self) -> MenuComponent:
        if self.hasNext():
            iterator: Iterator[MenuComponent] = self.stack[-1] if len(self.stack) != 0 else None
            component: MenuComponent = next(iterator)
            self.stack.append(component.createIterator())
            return component
        else:
            raise StopIteration
        
    def hasNext(self) -> bool:
        if len(self.stack) == 0:
            return False
        else:
            iterator: Iterator[MenuComponent] = self.stack[-1] if len(self.stack) != 0 else None
            if not iterator.hasNext():
                self.stack.pop()
                return self.hasNext()
            else:
                return True