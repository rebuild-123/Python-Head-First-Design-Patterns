from __future__ import annotations

from AbstractDuckFactory import AbstractDuckFactory
from CountingDuckFactory import CountingDuckFactory
from DuckCall import DuckCall
from Flock import Flock
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
            
        print("\nDuck Simulator: With Composite - Flocks")
        
        flockOfDucks: Flock = Flock()
        
        flockOfDucks.add(redheadDuck)
        flockOfDucks.add(duckCall)
        flockOfDucks.add(rubberDuck)
        flockOfDucks.add(gooseDuck)
        
        flockOfMallards: Flock = Flock()
        
        mallardOne: Quackable = duckFactory.createMallardDuck()
        mallardTwo: Quackable = duckFactory.createMallardDuck()
        mallardThree: Quackable = duckFactory.createMallardDuck()
        mallardFour: Quackable = duckFactory.createMallardDuck()
        
        flockOfMallards.add(mallardOne)
        flockOfMallards.add(mallardTwo)
        flockOfMallards.add(mallardThree)
        flockOfMallards.add(mallardFour)
        
        flockOfDucks.add(flockOfMallards)
    
        print("\nDuck Simulator: Whole Flock Simulation")
        self.simulate_(flockOfDucks)
        
        print("\nDuck Simulator: Mallard Flock Simulation")
        self.simulate_(flockOfMallards)
        
        print(f"The ducks quacked {QuackCounter.getQuacks()} times")
        
    # authors' java code has two "simulate", which cannot be translated to python.
    def simulate_(self, duck: Quackable) -> None:
        duck.quack()
        
if __name__ == "__main__":
    DuckSimulator.main()