from HasQuarterState import HasQuarterState
from NoQuarterState import NoQuarterState
from SoldOutState import SoldOutState
from SoldState import SoldState
from State import State
from WinnerState import WinnerState


class StringBuffer:
    def __init__(self):
        self.ls = []
        
    def append(self, string: str) -> None:
        self.ls.append(string)
        
    # toString
    def __str__(self) -> str:
        return ''.join(self.ls)

class GumballMachine:
    soldOutState: State
    noQuarterState: State
    hasQuarterState: State
    soldState: State
    winnerState: State
        
    state: State = SoldOutState
    count: int = 0
        
    def __init__(self, numberGumballs: int):
        self.soldOutState = SoldOutState(self)
        self.noQuarterState = NoQuarterState(self)
        self.hasQuarterState = HasQuarterState(self)
        self.soldState = SoldState(self)
        self.winnerState = WinnerState(self)
        
        self.count = numberGumballs
        if numberGumballs > 0:
            self.state = self.noQuarterState
            
    def insertQuarter(self) -> None:
        self.state.insertQuarter()
        
    def ejectQuarter(self) -> None:
        self.state.ejectQuarter()
        
    def turnCrank(self) -> None:
        self.state.turnCrank()
        self.state.dispense()
        
    def setState(self, state: State) -> None:
        self.state = state
        
    def releaseBall(self) -> None:
        print("A gumball comes rolling out the slot...")
        if self.count > 0:
            self.count -= 1
            
    def getCount(self) -> int:
        return self.count
    
    def refill(self, count: int) -> None:
        self.count += count
        print(f"The gumball machine was just refilled; its new count is: {self.count}")
        self.state.refill()
        
    def getState(self) -> State:
        return self.state
        
    def getSoldOutState(self) -> State:
        return self.soldOutState
    
    def getNoQuarterState(self) -> State:
        return self.noQuarterState
    
    def getHasQuarterState(self) -> State:
        return self.hasQuarterState
    
    def getSoldState(self) -> State:
        return self.soldState
    
    def getWinnerState(self) -> State:
        return self.winnerState
    
    # toString
    def __str__(self) -> str:
        result: StringBuffer = StringBuffer()
        result.append("\nMighty Gumball, Inc.")
        result.append("\nJava-enabled Standing Gumball Model #2004")
        result.append(f"\nInventory: {self.count} gumball")
        if self.count != 1:
            result.append("s")
        result.append("\n")
        result.append(f"Machine is {self.state}\n")
        return str(result)
    
    # toString for print
    def __repr__(self) -> str:
        return str(self)