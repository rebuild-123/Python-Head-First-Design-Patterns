from datetime import datetime
import random

from State import State


class HasQuarterState(State):
    randomWinner: random = random
    randomWinner.seed(int(datetime.now().strftime(".%f")[1:4]))
    # gumballMachine: GumballMachine # python does not allow GumballMachine and HasQuarterState to import each other.
    gumballMachine = None 
    
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
        
    def insertQuarter(self) -> None:
        print("You can't insert another quarter")
        
    def ejectQuarter(self) -> None:
        print("Quarter returned")
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
        
    def turnCrank(self) -> None:
        print("You turned...")
        winner: int = self.randomWinner.randint(0,9)
        if winner == 0 and self.gumballMachine.getCount() > 1:
            self.gumballMachine.setState(self.gumballMachine.getWinnerState())
        else:
            self.gumballMachine.setState(self.gumballMachine.getSoldState())
        
    def dispense(self) -> None:
        print("No gumball dispensed")
        
    def refill(self) -> None:
        pass
    
    # toString
    def __str__(self) -> str:
        return "waiting for turn of crank"
    
    # toString for print
    def __repr__(self) -> str:
        return str(self)