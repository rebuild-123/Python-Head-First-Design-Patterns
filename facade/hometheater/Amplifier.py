from StreamingPlayer import StreamingPlayer
from Tuner import Tuner


class Amplifier:
    description: str
    tuner: Tuner
    player: StreamingPlayer
        
    def __init__(self, description: str):
        self.description = description
        
    def on(self) -> None:
        print(f"{self.description} on")
        
    def off(self) -> None:
        print(f"{self.description} off")
        
    def setStereoSound(self) -> None:
        print(f"{self.description} stereo mode on")
        
    def setSurroundSound(self) -> None:
        print(f"{self.description} surround sound on (5 speakers, 1 subwoofer)")
        
    def setVolume(self, level: int) -> None:
        print(f"{self.description} setting volume to {level}")
        
    def setTuner(self, tuner: Tuner) -> None:
        print(f"{self.description} setting tuner to {tuner.toString()}")
        self.tuner = tuner
        
    def setStreamingPlayer(self, player: StreamingPlayer) -> None:
        print(f"{self.description} setting Streaming player to {player.toString()}")
        
    def toString(self) -> str:
        return self.description