class Light:
    location: str = ""
    level: int = 0
    
    def __init__(self, location: str):
        self.location = location
        
    def on(self) -> None:
        self.level = 100
        print("Light is on")
        
    def off(self) -> None:
        self.level = 0
        print("Light is off")
        
    def dim(self, level: int) -> None:
        self.level = level
        if level == 0:
            self.off()
        else:
            # print(f"Light is dimmed to {self.level}%") # authors' code
            self.on() # Not the authors' code. But this code can help show the results in the book.
        print() # Not the authors' code. But this code can help show the results in the book.
            
    def getLevel(self) -> int:
        return self.level