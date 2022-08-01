class TV:
    location: str
    channel: int = 0
        
    def __init__(self, location: str):
        self.location = location
        
    def on(self) -> None:
        print(f"{self.location} TV is on")
        
    def off(self) -> None:
        print(f"{self.location} TV is off")
        
    def setInputChannel(self) -> None:
        self.channel = 3
        print(f"{self.location} TV channel is set for DVD")