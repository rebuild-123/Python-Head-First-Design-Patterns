from typing import List, Optional

from Iterator import Iterator


class DinerMenuIterator(Iterator):
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
        if self.position >= len(self.items) or self.items[self.position] == None:
            return False
        else:
            return True