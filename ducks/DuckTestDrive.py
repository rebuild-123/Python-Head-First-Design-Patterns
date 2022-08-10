from Duck import Duck
from MallardDuck import MallardDuck
from Turkey import Turkey
from TurkeyAdapter import TurkeyAdapter
from WildTurkey import WildTurkey


class DuckTestDrive:
    @staticmethod
    def main(*args):
        duck: Duck = MallardDuck()
            
        turkey: Turkey = WildTurkey()
        turkeyAdapter: Duck = TurkeyAdapter(turkey)
            
        print("The Turkey says...")
        turkey.gobble()
        turkey.fly()
        
        print("\nThe Duck says...")
        DuckTestDrive.testDuck(duck)
        
        print("\nThe TurkeyAdapter says...")
        DuckTestDrive.testDuck(turkeyAdapter)
            
    @staticmethod
    def testDuck(duck: Duck) -> None:
        duck.quack()
        duck.fly()
        
if __name__ == "__main__":
    DuckTestDrive.main()