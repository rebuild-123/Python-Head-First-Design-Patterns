from typing import Iterator


class Iterator:
    def __init__(self, data):
        self.data = data
        self.idx = 0
        
    def hasNext(self) -> bool:
        return len(self.data) > self.idx
    
    def next(self):
        if len(self.data) > self.idx:
            temp = self.data[self.idx]
            self.idx += 1
            return temp
        else:
            return None

class Enumeration:
    def __init__(self, data) -> None:
        self.data = data
        self.idx = 0
        
    def hasMoreElements(self) -> bool:
        return len(self.data) > self.idx
    
    def nextElement(self):
        if len(self.data) > self.idx:
            temp = self.data[self.idx]
            self.idx += 1
            return temp
        else:
            return None
        
class UnsupportedOperationException(Exception):
    pass
        
class EnumerationIterator(Iterator):
    enumeration: Enumeration
    
    def __init__(self, enumeration: Enumeration):
        self.enumeration = enumeration
        
    def hasNext(self) -> bool:
        return self.enumeration.hasMoreElements()
    
    def next(self) -> object:
        return self.enumeration.nextElement()
    
    def remove(self) -> None:
        raise UnsupportedOperationException