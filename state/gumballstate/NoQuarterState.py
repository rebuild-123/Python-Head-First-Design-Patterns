from State import State


class NoQuarterState(State):
    # gumballMachine: GumballMachine # python does not allow GumballMachine and NoQuarterState to import each other.
    gumballMachine = None 
    
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
        
    def insertQuarter(self) -> None:
        print("You inserted a quarter")
        self.gumballMachine.setState(self.gumballMachine.getHasQuarterState())
        
    def ejectQuarter(self) -> None:
        print("You haven't inserted a quarter")
        
    def turnCrank(self) -> None:
        print("You turned, but there's no quarter")
        
    def dispense(self) -> None:
        print("You need to pay first")
        
    def refill(self) -> None:
        pass
    
    # toString
    def __str__(self) -> str:
        return "waiting for quarter"
    
    # toString for print
    def __repr__(self) -> str:
        return str(self)