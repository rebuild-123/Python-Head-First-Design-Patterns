from Amplifier import Amplifier

class CdPlayer:
    description: str
    currentTrack: int = 0
    amplifier: Amplifier
    title: str
        
    def __init__(self, description: str, amplifier: Amplifier):
        self.description = description
        self.amplifier = amplifier
        
    def on(self) -> None:
        print(f"{self.description} on")
        
    def off(self) -> None:
        print(f"{self.description} off")
        
    def play(self, title: str) -> None:
        self.title = title
        self.currentTrack = 0
        print(f"{self.description} playing \"{title}\"")
        
    # authors' java code has two "play", which cannot be translated to python.
    def play_track(self, track: int) -> None: 
        if self.title == None:
            print(f"{self.description} can't play track {self.currentTrack}, no cd inserted")
        else:
            self.currentTrack = track
            print(f"{self.description} playing track {self.currentChapter}")
            
    def stop(self) -> None:
        self.currentTrack = 0
        print(f"{self.description} stopped")
            
    def pause(self) -> None:
        self.currentChapter = 0
        print(f"{self.description} paused \"{self.title}\"")
        
    def toString(self) -> str:
        return self.description