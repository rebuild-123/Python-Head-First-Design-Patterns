from __future__ import annotations

from DuckCall import DuckCall
from MallardDuck import MallardDuck
from Quackable import Quackable
from RedheadDuck import RedheadDuck
from RubberDuck import RubberDuck


class DuckSimulator:
    @staticmethod
    def main(*args) -> None:
        simulator: DuckSimulator = DuckSimulator()
        simulator.simulate()
        
    def simulate(self) -> None:
        mallardDuck: Quackable = MallardDuck()
        redheadDuck: Quackable = RedheadDuck()
        duckCall: Quackable = DuckCall()
        rubberDuck: Quackable = RubberDuck()
            
        print("\nDuck Simulator")
    
        self.simulate_(mallardDuck)
        self.simulate_(redheadDuck)
        self.simulate_(duckCall)
        self.simulate_(rubberDuck)
        
    # authors' java code has two "simulate", which cannot be translated to python.
    def simulate_(self, duck: Quackable) -> None:
        duck.quack()
        
if __name__ == "__main__":
    DuckSimulator.main()