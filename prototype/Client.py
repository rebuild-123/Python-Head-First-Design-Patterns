from Dragon import Dragon
from Drakon import Drakon
from Monster import CloneNotSupportedException, Monster


class Client:
    @staticmethod
    def main(*args) -> None:
        p1: Monster = Dragon(name='Dragon_A', hasWings='True')
        p2: Monster = Drakon(name='Drakon_A', numHeads=2, canBreatheFire=True)
        # ... later ...
        Client.operation(p1)
        Client.operation(p2)
    
    @staticmethod
    def operation(p: Monster) -> Monster:
        # This code doesn't know or care what the concrete type of p is
        pCopy = None
        try:
            pCopy = p.copy()
            # do something useful with pCopy
            print("Operating with pCopy!")
        except CloneNotSupportedException as e:
            print(e)
        return pCopy
    
if __name__ == "__main__":
    Client.main()