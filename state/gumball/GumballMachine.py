from typing import Final


class StringBuffer:
    def __init__(self):
        self.ls = []
        
    def append(self, string: str) -> None:
        self.ls.append(string)
        
    # toString
    def __str__(self) -> str:
        return ''.join(self.ls)

class GumballMachine:
    SOLD_OUT: Final[int] = 0
    NO_QUARTER: Final[int] = 1
    HAS_QUARTER: Final[int] = 2
    SOLD: Final[int] = 3
    
    state: int = SOLD_OUT
    count: int = 0
        
    def __init__(self, count: int):
        self.count = count
        if self.count > 0:
            self.state = self.NO_QUARTER
            
    def insertQuarter(self) -> None:
        if self.state == self.HAS_QUARTER:
            print("You can't insert another quarter")
        elif self.state == self.NO_QUARTER:
            self.state = self.HAS_QUARTER
            print("You inserted a quarter")
        elif self.state == self.SOLD_OUT:
            print("You can't insert a quarter, the machine is sold out")
        elif self.state == self.SOLD:
            print("Please wait, we're already giving you a gumball")
            
    def ejectQuarter(self) -> None:
        if self.state == self.HAS_QUARTER:
            print("Quarter returned")
            self.state = self.NO_QUARTER
        elif self.state == self.NO_QUARTER:
            print("You haven't inserted a quarter")
        elif self.state == self.SOLD_OUT:
            print("Sorry, you already turned the crank")
        elif self.state == self.SOLD:
            print("You can't eject, you haven't inserted a quarter yet")
            
    def turnCrank(self) -> None:
        if self.state == self.SOLD:
            print("Turning twice doesn't get you another gumball!")
        elif self.state == self.NO_QUARTER:
            print("You turned but there's no quarter")
        elif self.state == self.SOLD_OUT:
            print("You turned, but there are no gumballs")
        elif self.state == self.HAS_QUARTER:
            print("You turned...")
            self.state = self.SOLD
            self.dispense()
            
    def dispense(self) -> None:
        if self.state == self.SOLD:
            print("A gumball comes rolling out the slot")
            self.count -= 1
            if self.count == 0: 
                print("Oops, out of gumballs!")
                self.state = self.SOLD_OUT
            else:
                self.state = self.NO_QUARTER
        elif self.state == self.NO_QUARTER:
            print("You need to pay first")
        elif self.state == self.SOLD_OUT:
            print("No gumball dispensed")
        elif self.state == self.HAS_QUARTER:
            print("No gumball dispensed")
            
    def refill(self, numGumBalls: int) -> None:
        self.count = numGumBalls
        self.state = self.NO_QUARTER
        
    # toString
    def __str__(self) -> str:
        result: StringBuffer = StringBuffer()
        result.append("\nMighty Gumball, Inc.")
        result.append(("\nJava-enabled Standing Gumball Model #2004\n"))
        result.append(f"Inventory: {self.count} gumball")
        if self.count != 1:
            result.append('s')
        result.append("\nMachine is ")
        if self.state == self.SOLD_OUT:
            result.append("sold out")
        elif self.state == self.NO_QUARTER:
            result.append("waiting for quarter")
        elif self.state == self.HAS_QUARTER:
            result.append("waiting for turn of crank")
        elif self.state == self.SOLD:
            result.append("delivering a gumball")
        result.append('\n')
        return str(result)
    
    # toString for print
    def __repr__(self):
        return str(self)