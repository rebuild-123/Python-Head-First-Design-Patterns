class Hottub:
    on_: bool
    temperature: int
        
    def __init__(self):
        pass
    
    def on(self) -> None:
        self.on_ = True
    
    def off(self) -> None:
        self.on_ = False
        
    def bubblesOn(self) -> None:
        if self.on_:
            print("Hottub is bubbling!")
        
    def bubblesOff(self) -> None:
        # if self.on_:
        if not self.on_:
            print("Hottub is not bubbling")
        
    def jetsOn(self) -> None:
        if self.on_:
            print("Hottub jets are on")
        
    def jetsOff(self) -> None:
        # if self.on_:
        if not self.on_:
            print("Hottub jets are off")
    
    def setTemperature(self, temperature: int) -> None:
        self.temperature = temperature
        
    def heat(self) -> None:
        self.temperature = 105
        print("Hottub is heating to a steaming 105 degrees")
        
    def cool(self) -> None:
        self.temperature = 98
        print("Hottub is cooling to 98 degrees")