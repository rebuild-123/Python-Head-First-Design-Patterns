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
        
class IteratorEnumeration(Enumeration):
    iterator: Iterator
    
    def __init__(self, iterator: Iterator):
        self.iterator = iterator
        
    def hasMoreElements(self) -> bool:
        return self.iterator.hasNext()
    
    def nextElement(self) -> object:
        return self.iterator.next()