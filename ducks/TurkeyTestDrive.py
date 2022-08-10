from Duck import Duck
from DuckAdapter import DuckAdapter
from MallardDuck import MallardDuck
from Turkey import Turkey


class TurkeyTestDrive:
    @staticmethod
    def main(*args):
        duck: Duck = MallardDuck()
        duckAdapter: Turkey = DuckAdapter(duck)
            
        for i in range(10):
            print("The DuckAdapter says...")
            duckAdapter.gobble()
            duckAdapter.fly()
        
if __name__ == "__main__":
    TurkeyTestDrive.main()