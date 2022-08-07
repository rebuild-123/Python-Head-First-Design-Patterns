from typing import List

from Iterator import Iterator
from MenuItem import MenuItem


class ArrayListIterator(Iterator):
    items: List[MenuItem]
    position: int = 0
        
    def __init__(self, items: List[MenuItem]):
        self.list = items
        
    # next
    def __next__(self) -> MenuItem:
        if self.hasNext():
            menuItem: MenuItem = self.items[self.position]
            self.position += 1
            return menuItem
        else:
            raise StopIteration
    
    def hasNext(self) -> bool:
        if self.position >= len(self.list):
            return False
        else:
            return True