from collections import UserList
from typing import List

# AbstractList provides a skeletal implementation of the List interface 
# to minimize the effort required to implement this interface backed by 
# a "random access" data store (such as an array). 

# To implement an unmodifiable list, the programmer needs only to extend 
# this class and provide implementations for the get(int) and size() methods.
# get(int index) is an abstract method in AbstractList
# size() is an abstract method in AbstractCollection
# subList(int fromIndex, int toIndex) returns a view of the portion of this list 
# between the specified fromIndex, inclusive, and toIndex, exclusive.


class MyStringList(UserList[str]):
    # __myList: List[str] # If you want to override "list" in python, the data must be stored in "data".
    data: List[str]
    def __init__(self, strings: List[str]):
        self.data = strings
    # public String get(int index)
    def __getitem__(self, index: int) -> str:
        return self.data[index]
    # public String set(int index, String item)
    def __setitem__(self, index: int, item: str) -> str:
        oldString = self.data[index]
        self.data[index] = item
        # print(oldString)
        return oldString
    # public int size()
    def __len__(self) -> int: 
        return len(self.data)