from State import State


class SoldState(State):
    # gumballMachine: GumballMachine # python does not allow GumballMachine and SoldState to import each other.
    gumballMachine = None 
    
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
        
    def insertQuarter(self) -> None:
        print("Please wait, we're already giving you a gumball")
        
    def ejectQuarter(self) -> None:
        print("Sorry, you already turned the crank")
        
    def turnCrank(self) -> None:
        print("Turning twice doesn't get you another gumball!")
        
    def dispense(self) -> None:
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount() > 0:
            self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
        else:
            print("Oops, out of gumballs!")
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())
        
    def refill(self) -> None:
        pass
    
    # toString
    def __str__(self) -> str:
        return "dispensing a gumball"
    
    # toString for print
    def __repr__(self) -> str:
        return str(self)