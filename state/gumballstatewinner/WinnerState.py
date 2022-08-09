from State import State


class WinnerState(State):
    # gumballMachine: GumballMachine # python does not allow GumballMachine and WinnerState to import each other.
    gumballMachine = None 
    
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
        
    def insertQuarter(self) -> None:
        print("Please wait, we're already giving you a Gumball")
        
    def ejectQuarter(self) -> None:
        print("Please wait, we're already giving you a Gumball")
        
    def turnCrank(self) -> None:
        print("Turning again doesn't get you another gumball!")
        
    def dispense(self) -> None:
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount() == 0:
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())
        else:
            self.gumballMachine.releaseBall()
            print("YOU'RE A WINNER! You got two gumballs for your quarter")
            if self.gumballMachine.getCount() > 0:
                self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
            else:
                print("Oops, out of gumballs!")
                self.gumballMachine.setState(self.gumballMachine.getSoldOutState())
        
    def refill(self) -> None:
        pass
    
    # toString
    def __str__(self) -> str:
        return "despensing two gumballs for your quarter, because YOU'RE A WINNER!"
    
    # toString for print
    def __repr__(self) -> str:
        return str(self)