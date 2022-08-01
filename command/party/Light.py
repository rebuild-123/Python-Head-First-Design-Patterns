class Light:
    location: str = ""
    level: int = 0
    
    def __init__(self, location: str):
        self.location = location
        
    def on(self) -> None:
        self.level = 100
        print(f'{self.location} light is on')
        
    def off(self) -> None:
        self.level = 0
        print(f'{self.location} light is off')
        
    def dim(self, level: int) -> None:
        self.level = level
        if level == 0:
            self.off()
        else:
            print(f"Light is dimmed to {level}%")
            
    def getLevel(self) -> int:
        return self.level