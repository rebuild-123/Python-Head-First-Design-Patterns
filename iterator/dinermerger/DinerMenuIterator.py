from typing import Iterator, List, Optional

from MenuItem import MenuItem


class DinerMenuIterator(Iterator[MenuItem]):
    items: List[MenuItem]
    position: int = 0
        
    def __init__(self, items: List[MenuItem]):
        self.items = items
        
    def __next__(self) -> Optional[MenuItem]:
        if self.hasNext():
            menuItem: MenuItem = self.items[self.position]
            self.position += 1
            return menuItem
        
            # or shorten to 
            # self.items[self.position := self.position+1]
        else:
            raise StopIteration
    
    def hasNext(self) -> bool:
        # if self.position >= len(self.items) or self.items[self.position] == None:
        #     return False
        # else:
        #     return True
        
        # or shorten to
        return len(self.items) > self.position