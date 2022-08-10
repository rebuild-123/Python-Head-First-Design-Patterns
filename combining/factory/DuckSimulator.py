from __future__ import annotations

from AbstractDuckFactory import AbstractDuckFactory
from CountingDuckFactory import CountingDuckFactory
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
        duckFactory: AbstractDuckFactory = CountingDuckFactory()
        simulator.simulate(duckFactory)
        
    def simulate(self, duckFactory: AbstractDuckFactory) -> None:
        mallardDuck: Quackable = duckFactory.createMallardDuck()
        redheadDuck: Quackable = duckFactory.createRedheadDuck()
        duckCall: Quackable = duckFactory.createDuckCall()
        rubberDuck: Quackable = duckFactory.createRubberDuck()
        gooseDuck: Quackable = GooseAdapter(Goose())
            
        print("\nDuck Simulator: With Abstract Factory")
    
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