class Light:
    location: str = ""
    
    def __init__(self, location: str):
        self.location = location
        
    def on(self) -> None:
        print(f'{self.location} light is on')
        
    def off(self) -> None:
        print(f'{self.location} light is off')