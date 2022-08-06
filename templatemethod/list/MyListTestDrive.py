from typing import List

from MyStringList import MyStringList


class MyListTestDrive:
    
    @staticmethod
    def main(*args) -> None:
        ducks: List[str] = ["Mallard Duck", "Redhead Duck", "Rubber Duck", "Decoy Duck"]
        ducksList: MyStringList = MyStringList(ducks)
        for i in range(len(ducksList)):
            print(ducksList[i])
        oldDuck: str = ducksList.__setitem__(index=3, item="Donald Duck")
        print(f"Replacing {oldDuck}")
        print("New List:")
        for i in range(len(ducksList)):
            print(ducksList[i])
        # Now the real test... subList()
        ducksSubList: list = ducksList[2:3]
        print(f"Created a sub list of ducks, with size: {len(ducksSubList)}")
        for i in range(len(ducksSubList)):
            print(ducksSubList[i])
            
if __name__ == "__main__":
    MyListTestDrive.main()