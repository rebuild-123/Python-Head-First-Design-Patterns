from typing import List


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
        
class Collections:
    @staticmethod
    def main(args: List[str]) -> None:
        v = args
        print("Using enumeration with Vector")
        enumeration: Enumeration = Enumeration(v)
        while enumeration.hasMoreElements():
            print(enumeration.nextElement())
        print("Using iterator with Vector")
        iterator: Iterator = Iterator(v)
        while iterator.hasNext():
            print(iterator.next())
        print("Using for/in with array of Strings")
        for color in args:
            print(color)
            
if __name__ == "__main__":
    Collections.main(['a', 'b', 'c'])