from typing import List, Optional

from Iterator import Iterator


class IllegalStateException(Exception): pass

class PancakeHouseMenuIterator(Iterator):
    items: List[str]
    position: int = 0
        
    def __init__(self, items: List[str]):
        self.items = items
        
    def __next__(self) -> Optional[str]:
        if self.hasNext():
            menuItem: str = self.items[self.position]
            self.position += 1
            return menuItem
        else:
            raise StopIteration
    
    def hasNext(self) -> bool:
        if self.position >= len(self.items):
            return False
        else:
            return True