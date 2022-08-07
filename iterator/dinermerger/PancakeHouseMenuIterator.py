from typing import List

from Iterator import Iterator
from MenuItem import MenuItem


class PancakeHouseMenuIterator(Iterator):
    items: List[MenuItem]
    position: int = 0
        
    def __init__(self, items: List[MenuItem]):
        self.items = items
        
    # next
    def __next__(self) -> MenuItem:
        if self.hasNext():
            menuItem: MenuItem = self.items[self.position]
            self.position += 1
            return menuItem
        
            # or shorten to 
            # self.items[self.position := self.position+1]
        else:
            raise StopIteration
    
    def hasNext(self) -> bool:
        # if self.position >= len(self.list):
        #     return False
        # else:
        #     return True
        # or shorten to
        return len(self.items) > self.position