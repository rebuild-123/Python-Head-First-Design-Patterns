from __future__ import annotations

from DuckCall import DuckCall
from Goose import Goose
from GooseAdapter import GooseAdapter
from MallardDuck import MallardDuck
from Quackable import Quackable
from QuackCounter import QuackCounter
from RedheadDuck import RedheadDuck
from RubberDuck import RubberDuck


class DuckSimulator:
    @staticmethod
    def main(*args) -> None:
        simulator: DuckSimulator = DuckSimulator()
        simulator.simulate()
        
    def simulate(self) -> None:
        mallardDuck: Quackable = QuackCounter(MallardDuck())
        redheadDuck: Quackable = QuackCounter(RedheadDuck())
        duckCall: Quackable = QuackCounter(DuckCall())
        rubberDuck: Quackable = QuackCounter(RubberDuck())
        gooseDuck: Quackable = GooseAdapter(Goose())
            
        print("\nDuck Simulator")
    
        self.simulate_(mallardDuck)
        self.simulate_(redheadDuck)
        self.simulate_(duckCall)
        self.simulate_(rubberDuck)
        self.simulate_(gooseDuck)
        
        print(f"The ducks quacked {QuackCounter.getQuacks()} times")
        
    # authors' java code has two "simulate", which cannot be translated to python.
    def simulate_(self, duck: Quackable) -> None:
        duck.quack()
        
if __name__ == "__main__":
    DuckSimulator.main()