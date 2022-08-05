class Tuner:
    description: str
    # amplifier: Amplifier # Python does not allow Tuner and Amplifier to import each other.
    frequency: float
        
    def __init__(self, description: str, amplifier):
        self.description = description
        
    def on(self) -> None:
        print(f"{self.description} on")
        
    def off(self) -> None:
        print(f"{self.description} off")
        
    def setFrequency(self, frequency: float) -> None:
        print(f"{self.description} setting frequency to {frequency}")
        self.frequency = frequency
        
    def setAm(self) -> None:
        print(f'{self.description} setting AM mode')
        
    def setFm(self) -> None:
        print(f'{self.description} setting FM mode')
        
    def toString(self) -> str:
        return self.description