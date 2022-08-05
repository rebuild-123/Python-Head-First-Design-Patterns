class StreamingPlayer:
    description: str
    currentChapter: int = 0
    # amplifier: Amplifier # Python does not allow StreamingPlayer and Amplifier to import each other.
    movie: str = None
        
    def __init__(self, description: str, amplifier):
        self.description = description
        self.amplifier = amplifier
        
    def on(self) -> None:
        print(f"{self.description} on")
        
    def off(self) -> None:
        print(f"{self.description} off")
        
    def play(self, movie: str) -> None:
        self.movie = movie
        self.currentChapter = 0
        print(f"{self.description} playing \"{movie}\"")
        
    # authors' java code has two "play", which cannot be translated to python.
    def play_chapter(self, chapter: int) -> None: 
        if self.movie == None:
            print(f"{self.description} can't play chapter {chapter} no movie selected")
        else:
            self.currentChapter = chapter
            print(f"{self.description} playing chapter {self.currentChapter} of \"{self.movie}\"")
            
    def stop(self) -> None:
        self.currentChapter = 0
        print(f"{self.description} stopped \"{self.movie}\"")
            
    def pause(self) -> None:
        self.currentChapter = 0
        print(f"{self.description} paused \"{self.movie}\"")
        
    def setTwoChannelAudio(self) -> None:
        print(f"{self.description} set two channel audio")
        
    def setSurroundAudio(self) -> None:
        print(f"{self.description} set surround audio")
        
    def toString(self) -> str:
        return self.description