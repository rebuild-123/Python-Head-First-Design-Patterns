class Light:
    location: str = ""
    
    def __init__(self):
        pass
        
    def on(self) -> None:
        print("Light is on")
        
    def off(self) -> None:
        print("Light is off")