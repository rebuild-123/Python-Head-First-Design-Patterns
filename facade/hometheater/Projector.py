from StreamingPlayer import StreamingPlayer

class Projector:
    description: str
    player: StreamingPlayer
        
    def __init__(self, description: str, player: StreamingPlayer):
        self.description = description
        self.player = player
        
    def on(self) -> None:
        print(f"{self.description} on")
        
    def off(self) -> None:
        print(f"{self.description} off")
        
    def wideScreenMode(self) -> None:
        print(f"{self.description} in widescreen mode (16x9 aspect ratio)")
        
    def tvMode(self) -> None:
        print(f"{self.description} in tv mode (4x3 aspect ratio)")
        
    def toString(self) -> str:
        return self.description