from State import State


class SoldOutState(State):
    # gumballMachine: GumballMachine # python does not allow GumballMachine and SoldOutState to import each other.
    gumballMachine = None 
    
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
        
    def insertQuarter(self) -> None:
        print("You can't insert a quarter, the machine is sold out")
        
    def ejectQuarter(self) -> None:
        print("You can't eject, you haven't inserted a quarter yet")
        
    def turnCrank(self) -> None:
        print("You turned, but there are no gumballs")
        
    def dispense(self) -> None:
        print("No gumball dispensed")
        
    def refill(self) -> None:
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
    
    # toString
    def __str__(self) -> str:
        return "sold out"
    
    # toString for print
    def __repr__(self) -> str:
        return str(self)