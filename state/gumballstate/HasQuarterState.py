from State import State


class HasQuarterState(State):
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