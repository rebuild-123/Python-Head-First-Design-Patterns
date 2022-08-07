from datetime import datetime
from typing import List

from Iterator import Iterator
from MenuItem import MenuItem


class AlternatingDinerMenuIterator(Iterator):
    list: List[MenuItem]
    position: int = 0
        
    def __init__(self, list: List[MenuItem]):
        self.list = list
        self.position = datetime.weekday(datetime.now()) % 2
        
    # next
    def __next__(self) -> MenuItem:
        if self.hasNext():
            menuItem: MenuItem = self.list[self.position]
            self.position += 2
            return menuItem
        else:
            raise StopIteration
    
    def hasNext(self) -> bool:
        if self.position >= len(self.list) or self.list[self.position] == None:
            return False
        else:
            return True
        
    # toString
    def __str__(self) -> str:
        return "Alternating Diner Menu Iterator"