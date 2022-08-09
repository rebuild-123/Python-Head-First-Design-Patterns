from GumballMachine import GumballMachine


class GumballMachineTestDrive:
    
    @staticmethod
    def main(*args) -> None:
        gumballMachine: GumballMachine = GumballMachine(5)
            
        print(gumballMachine)
        
        gumballMachine.insertQuarter()
        gumballMachine.turnCrank();
        
        print(gumballMachine)
        
        gumballMachine.insertQuarter()
        gumballMachine.ejectQuarter()
        gumballMachine.turnCrank()
        
        print(gumballMachine)
        
        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()
        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()
        gumballMachine.ejectQuarter();
        
        print(gumballMachine)
        
        gumballMachine.insertQuarter()
        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()
        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()
        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()
        
        print(gumballMachine)
        
if __name__ == "__main__":
    GumballMachineTestDrive.main()