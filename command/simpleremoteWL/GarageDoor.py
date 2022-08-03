class GarageDoor:
    location: str
    
    def __init__(self):
        pass
        
    def up(self) -> None:
        print("Garage Door is Open")
        
    def down(self) -> None:
        print("Garage Door is Closed")
        
    def stop(self) -> None:
        print("Garage Door is Stopped")
        
    def lightOn(self) -> None:
        print("Garage light is on")
        
    def lightOff(self) -> None:
        print("Garage light is off")