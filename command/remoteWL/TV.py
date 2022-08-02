class TV:
    location: str
    channel: int
        
    def __init__(self, location: str):
        self.location = location
        
    def on(self) -> None:
        print("TV is on")
        
    def off(self) -> None:
        print("TV is off")
        
    def setInputChannel(self) -> None:
        self.channel = 3
        print("Channel is set for VCR")