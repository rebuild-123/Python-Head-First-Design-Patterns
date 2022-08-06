from typing import List

from Duck import Duck


class DuckSortTestDrive:
    
    @staticmethod
    def main(*args) -> None:
        ducks: List[Duck] = [
            Duck("Daffy", 8),
            Duck("Dewey", 2),
            Duck("Howard", 7),
            Duck("Louie", 2),
            Duck("Donald", 10),
            Duck("Huey", 2)
        ]
        
        print("Before sorting:")
        DuckSortTestDrive.display(ducks)
        ducks = sorted(ducks)
        print("\nAfter sorting:")
        DuckSortTestDrive.display(ducks)
        
    @staticmethod
    def display(ducks: List[Duck]) -> None:
        for d in ducks:
            print(d)
        
if __name__ == "__main__":
    DuckSortTestDrive.main()