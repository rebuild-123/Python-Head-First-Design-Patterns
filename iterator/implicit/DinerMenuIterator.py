from typing import Iterator, List, Optional

from MenuItem import MenuItem


class IllegalStateException(Exception): pass

class DinerMenuIterator(Iterator[MenuItem]):
    list: List[MenuItem]
    position: int = 0
        
    def __init__(self, list: List[MenuItem]):
        self.list = list
        
    def __next__(self) -> Optional[MenuItem]:
        if self.hasNext():
            menuItem: MenuItem = self.list[self.position]
            self.position += 1
            return menuItem
        else:
            raise StopIteration
    
    def hasNext(self) -> bool:
        if self.position >= len(self.list) or self.list[self.position] == None:
            return False
        else:
            return True
        
    def remove(self) -> None:
        if self.position <= 0:
            raise IllegalStateException("You can't remove an item until you've done at least one next()")
        if self.list[self.position-1] != None:
            for i in range(self.position-1, len(self.list)-1):
                self.list[i] = self.list[i+1]
            self.list[len(self.list)-1] = None