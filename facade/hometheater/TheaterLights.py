class TheaterLights:
    description: str
        
    def __init__(self, description: str):
        self.description = description
        
    def on(self) -> None:
        print(f'{self.description} on')
        
    def off(self) -> None:
        print(f'{self.description} off')
        
    def dim(self, level: int) -> None:
        print(f"{self.description} dimming to {level}%")
        
    def toString(self) -> None:
        return self.description