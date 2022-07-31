class GarageDoor:
    location: str
    
    def __init__(self, location: str):
        self.location = location
        
    def up(self) -> None:
        print(f'{self.location} garage Door is Up')
        
    def down(self) -> None:
        print(f'{self.location} garage Door is Down')
        
    def stop(self) -> None:
        print(f'{self.location} garage Door is Stopped')
        
    def lightOn(self) -> None:
        print(f'{self.location} garage light is on')
        
    def lightOff(self) -> None:
        print(f'{self.location} garage light is off')