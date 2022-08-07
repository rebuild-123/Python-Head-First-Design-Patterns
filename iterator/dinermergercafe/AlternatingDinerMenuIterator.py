from datetime import datetime
from typing import List

from Iterator import Iterator
from MenuItem import MenuItem


class UnsupportedOperationException(Exception): pass

class AlternatingDinerMenuIterator(Iterator):
    items: List[MenuItem]
    position: int = 0
        
    def __init__(self, items: List[MenuItem]):
        self.items = items
        self.position = datetime.weekday(datetime.now()) % 2
        
    # next
    def __next__(self) -> MenuItem:
        if self.hasNext():
            menuItem: MenuItem = self.items[self.position]
            self.position += 2
            return menuItem
        else:
            raise StopIteration
    
    def hasNext(self) -> bool:
        if self.position >= len(self.items) or self.items[self.position] == None:
            return False
        else:
            return True
        
    def remove(self) -> None:
        raise UnsupportedOperationException("Alternating Diner Menu Iterator does not support remove()")