class Hottub:
    on_: bool
    temperature: int = 0
        
    def __init__(self):
        pass
    
    def on(self) -> None:
        self.on_ = True
    
    def off(self) -> None:
        self.on_ = False
        
    def circulate(self) -> None:
        if self.on_:
            print("Hottub is bubbling!")
        
    def jetsOn(self) -> None:
        if self.on_:
            print("Hottub jets are on")
        
    def jetsOff(self) -> None:
        # if self.on_:
        if not self.on_:
            print("Hottub jets are off")
    
    def setTemperature(self, temperature: int) -> None:
        if temperature > self.temperature:
            print(f"Hottub is heating to a steaming {temperature} degrees")
        else:
            print(f"Hottub is cooling to {temperature} degrees")
        self.temperature = temperature