from Duck import Duck
from Turkey import Turkey


class TurkeyAdapter(Duck):
    turkey: Turkey
    
    def __init__(self, turkey: Turkey):
        self.turkey = turkey
        
    def quack(self) -> None:
        self.turkey.gobble()
        
    def fly(self) -> None:
        for i in range(5):
            self.turkey.fly()